"""Network Authentication Helpers

Contains interface (MultiDomainBasicAuth) and associated glue code for
providing credentials in the context of network requests.
"""

import logging
import urllib.parse
from typing import Any, Dict, List, Optional, Tuple

from pip._vendor.requests.auth import AuthBase, HTTPBasicAuth
from pip._vendor.requests.models import Request, Response
from pip._vendor.requests.utils import get_netrc_auth

from pip._internal.utils.misc import (
    ask,
    ask_input,
    ask_password,
    remove_auth_from_url,
    split_auth_netloc_from_url,
)
from pip._internal.vcs.versioncontrol import AuthInfo

logger = logging.getLogger(__name__)

Credentials = Tuple[str, str, str]

try:
    import keyring
except ImportError:
    keyring = None
except Exception as exc:
    logger.warning(
        "Keyring is skipped due to an exception: %s", str(exc),
    )
    keyring = None


def get_keyring_auth(url, username):
    # type: (Optional[str], Optional[str]) -> Optional[AuthInfo]
    """Return the tuple auth for a given url from keyring."""
    global keyring
    if not url or not keyring:
        return None

    try:
        try:
            get_credential = keyring.get_credential
        except AttributeError:
            pass
        else:
            logger.debug("Getting credentials from keyring for %s", url)
            cred = get_credential(url, username)
            if cred is not None:
                return cred.username, cred.password
            return None

        if username:
            logger.debug("Getting password from keyring for %s", url)
            password = keyring.get_password(url, username)
            if password:
                return username, password

    except Exception as exc:
        logger.warning(
            "Keyring is skipped due to an exception: %s", str(exc),
        )
        keyring = None
    return None


class MultiDomainBasicAuth(AuthBase):

    def __init__(self, prompting=True, index_urls=None):
        # type: (bool, Optional[List[str]]) -> None
        self.prompting = prompting
        self.index_urls = index_urls
        self.passwords = {}  # type: Dict[str, AuthInfo]
        # When the user is prompted to enter credentials and keyring is
        # available, we will offer to save them. If the user accepts,
        # this value is set to the credentials they entered. After the
        # request authenticates, the caller should call
        # ``save_credentials`` to save these.
        self._credentials_to_save = None  # type: Optional[Credentials]

    def _get_index_url(self, url):
        # type: (str) -> Optional[str]
        """Return the original index URL matching the requested URL.

        Cached or dynamically generated credentials may work against
        the original index URL rather than just the netloc.

        The provided url should have had its username and password
        removed already. If the original index url had credentials then
        they will be included in the return value.

        Returns None if no matching index was found, or if --no-index
        was specified by the user.
        """
        if not url or not self.index_urls:
            return None

        for u in self.index_urls:
            prefix = remove_auth_from_url(u).rstrip("/") + "/"
            if url.startswith(prefix):
                return u
        return None

    def _get_new_credentials(self, original_url, allow_netrc=True,
                             allow_keyring=False):
        # type: (str, bool, bool) -> AuthInfo
        """Find and return credentials for the specified URL."""
        # Split the credentials and netloc from the url.
        url, netloc, url_user_password = split_auth_netloc_from_url(
            original_url,
        )

        # Start with the credentials embedded in the url
        username, password = url_user_password
        if username is not None and password is not None:
            logger.debug("Found credentials in url for %s", netloc)
            return url_user_password

        # Find a matching index url for this request
        index_url = self._get_index_url(url)
        if index_url:
            # Split the credentials from the url.
            index_info = split_auth_netloc_from_url(index_url)
            if index_info:
                index_url, _, index_url_user_password = index_info
                logger.debug("Found index url %s", index_url)

        # If an index URL was found, try its embedded credentials
        if index_url and index_url_user_password[0] is not None:
            username, password = index_url_user_password
            if username is not None and password is not None:
                logger.debug("Found credentials in index url for %s", netloc)
                return index_url_user_password

        # Get creds from netrc if we still don't have them
        if allow_netrc:
            netrc_auth = get_netrc_auth(original_url)
            if netrc_auth:
                logger.debug("Found credentials in netrc for %s", netloc)
                return netrc_auth

        # If we don't have a password and keyring is available, use it.
        if allow_keyring:
            # The index url is more specific than the netloc, so try it first
            kr_auth = (
                get_keyring_auth(index_url, username) or
                get_keyring_auth(netloc, username)
            )
            if kr_auth:
                logger.debug("Found credentials in keyring for %s", netloc)
                return kr_auth

        return username, password

    def _get_url_and_credentials(self, original_url):
        # type: (str) -> Tuple[str, Optional[str], Optional[str]]
        """Return the credentials to use for the provided URL.

        If allowed, netrc and keyring may be used to obtain the
        correct credentials.

        Returns (url_without_credentials, username, password). Note
        that even if the original URL contains credentials, this
        function may return a different username and password.
        """
        url, netloc, _ = split_auth_netloc_from_url(original_url)

        # Use any stored credentials that we have for this netloc
        username, password = self.passwords.get(netloc, (None, None))

        if username is None and password is None:
            # No stored credentials. Acquire new credentials without prompting
            # the user. (e.g. from netrc, keyring, or the URL itself)
            username, password = self._get_new_credentials(original_url)

        if username is not None or password is not None:
            # Convert the username and password if they're None, so that
            # this netloc will show up as "cached" in the conditional above.
            # Further, HTTPBasicAuth doesn't accept None, so it makes sense to
            # cache the value that is going to be used.
            username = username or ""
            password = password or ""

            # Store any acquired credentials.
            self.passwords[netloc] = (username, password)

        assert (
            # Credentials were found
            (username is not None and password is not None) or
            # Credentials were not found
            (username is None and password is None)
        ), f"Could not load credentials from url: {original_url}"

        return url, username, password

    def __call__(self, req):
        # type: (Request) -> Request
        # Get credentials for this request
        url, username, password = self._get_url_and_credentials(req.url)

        # Set the url of the request to the url without any credentials
        req.url = url

        if username is not None and password is not None:
            # Send the basic auth with this request
            req = HTTPBasicAuth(username, password)(req)

        # Attach a hook to handle 401 responses
        req.register_hook("response", self.handle_401)

        return req

    # Factored out to allow for easy patching in tests
    def _prompt_for_password(self, netloc):
        # type: (str) -> Tuple[Optional[str], Optional[str], bool]
        username = ask_input(f"User for {netloc}: ")
        if not username:
            return None, None, False
        auth = get_keyring_auth(netloc, username)
        if auth and auth[0] is not None and auth[1] is not None:
            return auth[0], auth[1], False
        password = ask_password("Password: ")
        return username, password, True

    # Factored out to allow for easy patching in tests
    def _should_save_password_to_keyring(self):
        # type: () -> bool
        if not keyring:
            return False
        return ask("Save credentials to keyring [y/N]: ", ["y", "n"]) == "y"

    def handle_401(self, resp, **kwargs):
        # type: (Response, **Any) -> Response
        # We only care about 401 responses, anything else we want to just
        #   pass through the actual response
        if resp.status_code != 401:
            return resp

        # We are not able to prompt the user so simply return the response
        if not self.prompting:
            return resp

        parsed = urllib.parse.urlparse(resp.url)

        # Query the keyring for credentials:
        username, password = self._get_new_credentials(resp.url,
                                                       allow_netrc=False,
                                                       allow_keyring=True)

        # Prompt the user for a new username and password
        save = False
        if not username and not password:
            username, password, save = self._prompt_for_password(parsed.netloc)

        # Store the new username and password to use for future requests
        self._credentials_to_save = None
        if username is not None and password is not None:
            self.passwords[parsed.netloc] = (username, password)

            # Prompt to save the password to keyring
            if save and self._should_save_password_to_keyring():
                self._credentials_to_save = (parsed.netloc, username, password)

        # Consume content and release the original connection to allow our new
        #   request to reuse the same one.
        resp.content
        resp.raw.release_conn()

        # Add our new username and password to the request
        req = HTTPBasicAuth(username or "", password or "")(resp.request)
        req.register_hook("response", self.warn_on_401)

        # On successful request, save the credentials that were used to
        # keyring. (Note that if the user responded "no" above, this member
        # is not set and nothing will be saved.)
        if self._credentials_to_save:
            req.register_hook("response", self.save_credentials)

        # Send our new request
        new_resp = resp.connection.send(req, **kwargs)
        new_resp.history.append(resp)

        return new_resp

    def warn_on_401(self, resp, **kwargs):
        # type: (Response, **Any) -> None
        """Response callback to warn about incorrect credentials."""
        if resp.status_code == 401:
            logger.warning(
                '401 Error, Credentials not correct for %s', resp.request.url,
            )

    def save_credentials(self, resp, **kwargs):
        # type: (Response, **Any) -> None
        """Response callback to save credentials on success."""
        assert keyring is not None, "should never reach here without keyring"
        if not keyring:
            return

        creds = self._credentials_to_save
        self._credentials_to_save = None
        if creds and resp.status_code < 400:
            try:
                logger.info('Saving credentials to keyring')
                keyring.set_password(*creds)
            except Exception:
                logger.exception('Failed to save credentials')
