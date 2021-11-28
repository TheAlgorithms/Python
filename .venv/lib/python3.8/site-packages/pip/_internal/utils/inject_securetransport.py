"""A helper module that injects SecureTransport, on import.

The import should be done as early as possible, to ensure all requests and
sessions (or whatever) are created after injecting SecureTransport.

Note that we only do the injection on macOS, when the linked OpenSSL is too
old to handle TLSv1.2.
"""

import sys


def inject_securetransport():
    # type: () -> None
    # Only relevant on macOS
    if sys.platform != "darwin":
        return

    try:
        import ssl
    except ImportError:
        return

    # Checks for OpenSSL 1.0.1
    if ssl.OPENSSL_VERSION_NUMBER >= 0x1000100F:
        return

    try:
        from pip._vendor.urllib3.contrib import securetransport
    except (ImportError, OSError):
        return

    securetransport.inject_into_urllib3()


inject_securetransport()
