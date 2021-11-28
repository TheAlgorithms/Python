import sys

try:
    # Our match_hostname function is the same as 3.5's, so we only want to
    # import the match_hostname function if it's at least that good.
    if sys.version_info < (3, 5):
        raise ImportError("Fallback to vendored code")

    from ssl import CertificateError, match_hostname
except ImportError:
    try:
        # Backport of the function from a pypi module
        from backports.ssl_match_hostname import (  # type: ignore
            CertificateError,
            match_hostname,
        )
    except ImportError:
        # Our vendored copy
        from ._implementation import CertificateError, match_hostname  # type: ignore

# Not needed, but documenting what we provide.
__all__ = ("CertificateError", "match_hostname")
