import json
import logging
from typing import Optional

from pip._vendor.pkg_resources import Distribution

from pip._internal.models.direct_url import (
    DIRECT_URL_METADATA_NAME,
    ArchiveInfo,
    DirectUrl,
    DirectUrlValidationError,
    DirInfo,
    VcsInfo,
)
from pip._internal.models.link import Link
from pip._internal.vcs import vcs

logger = logging.getLogger(__name__)


def direct_url_as_pep440_direct_reference(direct_url, name):
    # type: (DirectUrl, str) -> str
    """Convert a DirectUrl to a pip requirement string."""
    direct_url.validate()  # if invalid, this is a pip bug
    requirement = name + " @ "
    fragments = []
    if isinstance(direct_url.info, VcsInfo):
        requirement += "{}+{}@{}".format(
            direct_url.info.vcs, direct_url.url, direct_url.info.commit_id
        )
    elif isinstance(direct_url.info, ArchiveInfo):
        requirement += direct_url.url
        if direct_url.info.hash:
            fragments.append(direct_url.info.hash)
    else:
        assert isinstance(direct_url.info, DirInfo)
        requirement += direct_url.url
    if direct_url.subdirectory:
        fragments.append("subdirectory=" + direct_url.subdirectory)
    if fragments:
        requirement += "#" + "&".join(fragments)
    return requirement


def direct_url_from_link(link, source_dir=None, link_is_in_wheel_cache=False):
    # type: (Link, Optional[str], bool) -> DirectUrl
    if link.is_vcs:
        vcs_backend = vcs.get_backend_for_scheme(link.scheme)
        assert vcs_backend
        url, requested_revision, _ = vcs_backend.get_url_rev_and_auth(
            link.url_without_fragment
        )
        # For VCS links, we need to find out and add commit_id.
        if link_is_in_wheel_cache:
            # If the requested VCS link corresponds to a cached
            # wheel, it means the requested revision was an
            # immutable commit hash, otherwise it would not have
            # been cached. In that case we don't have a source_dir
            # with the VCS checkout.
            assert requested_revision
            commit_id = requested_revision
        else:
            # If the wheel was not in cache, it means we have
            # had to checkout from VCS to build and we have a source_dir
            # which we can inspect to find out the commit id.
            assert source_dir
            commit_id = vcs_backend.get_revision(source_dir)
        return DirectUrl(
            url=url,
            info=VcsInfo(
                vcs=vcs_backend.name,
                commit_id=commit_id,
                requested_revision=requested_revision,
            ),
            subdirectory=link.subdirectory_fragment,
        )
    elif link.is_existing_dir():
        return DirectUrl(
            url=link.url_without_fragment,
            info=DirInfo(),
            subdirectory=link.subdirectory_fragment,
        )
    else:
        hash = None
        hash_name = link.hash_name
        if hash_name:
            hash = f"{hash_name}={link.hash}"
        return DirectUrl(
            url=link.url_without_fragment,
            info=ArchiveInfo(hash=hash),
            subdirectory=link.subdirectory_fragment,
        )


def dist_get_direct_url(dist):
    # type: (Distribution) -> Optional[DirectUrl]
    """Obtain a DirectUrl from a pkg_resource.Distribution.

    Returns None if the distribution has no `direct_url.json` metadata,
    or if `direct_url.json` is invalid.
    """
    if not dist.has_metadata(DIRECT_URL_METADATA_NAME):
        return None
    try:
        return DirectUrl.from_json(dist.get_metadata(DIRECT_URL_METADATA_NAME))
    except (
        DirectUrlValidationError,
        json.JSONDecodeError,
        UnicodeDecodeError,
    ) as e:
        logger.warning(
            "Error parsing %s for %s: %s",
            DIRECT_URL_METADATA_NAME,
            dist.project_name,
            e,
        )
        return None
