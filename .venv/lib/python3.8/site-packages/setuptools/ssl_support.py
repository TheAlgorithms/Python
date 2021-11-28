import os
import socket
import atexit
import re
import functools
import urllib.request
import http.client


from pkg_resources import ResolutionError, ExtractionError

try:
    import ssl
except ImportError:
    ssl = None

__all__ = [
    'VerifyingHTTPSHandler', 'find_ca_bundle', 'is_available', 'cert_paths',
    'opener_for'
]

cert_paths = """
/etc/pki/tls/certs/ca-bundle.crt
/etc/ssl/certs/ca-certificates.crt
/usr/share/ssl/certs/ca-bundle.crt
/usr/local/share/certs/ca-root.crt
/etc/ssl/cert.pem
/System/Library/OpenSSL/certs/cert.pem
/usr/local/share/certs/ca-root-nss.crt
/etc/ssl/ca-bundle.pem
""".strip().split()

try:
    HTTPSHandler = urllib.request.HTTPSHandler
    HTTPSConnection = http.client.HTTPSConnection
except AttributeError:
    HTTPSHandler = HTTPSConnection = object

is_available = ssl is not None and object not in (
    HTTPSHandler, HTTPSConnection)


try:
    from ssl import CertificateError, match_hostname
except ImportError:
    try:
        from backports.ssl_match_hostname import CertificateError
        from backports.ssl_match_hostname import match_hostname
    except ImportError:
        CertificateError = None
        match_hostname = None

if not CertificateError:

    class CertificateError(ValueError):
        pass


if not match_hostname:  # noqa: C901  # 'If 59' is too complex (21)  # FIXME

    def _dnsname_match(dn, hostname, max_wildcards=1):
        """Matching according to RFC 6125, section 6.4.3

        https://tools.ietf.org/html/rfc6125#section-6.4.3
        """
        pats = []
        if not dn:
            return False

        # Ported from python3-syntax:
        # leftmost, *remainder = dn.split(r'.')
        parts = dn.split(r'.')
        leftmost = parts[0]
        remainder = parts[1:]

        wildcards = leftmost.count('*')
        if wildcards > max_wildcards:
            # Issue #17980: avoid denials of service by refusing more
            # than one wildcard per fragment.  A survey of established
            # policy among SSL implementations showed it to be a
            # reasonable choice.
            raise CertificateError(
                "too many wildcards in certificate DNS name: " + repr(dn))

        # speed up common case w/o wildcards
        if not wildcards:
            return dn.lower() == hostname.lower()

        # RFC 6125, section 6.4.3, subitem 1.
        # The client SHOULD NOT attempt to match a
        # presented identifier in which the wildcard
        # character comprises a label other than the
        # left-most label.
        if leftmost == '*':
            # When '*' is a fragment by itself, it matches a non-empty dotless
            # fragment.
            pats.append('[^.]+')
        elif leftmost.startswith('xn--') or hostname.startswith('xn--'):
            # RFC 6125, section 6.4.3, subitem 3.
            # The client SHOULD NOT attempt to match a presented identifier
            # where the wildcard character is embedded within an A-label or
            # U-label of an internationalized domain name.
            pats.append(re.escape(leftmost))
        else:
            # Otherwise, '*' matches any dotless string, e.g. www*
            pats.append(re.escape(leftmost).replace(r'\*', '[^.]*'))

        # add the remaining fragments, ignore any wildcards
        for frag in remainder:
            pats.append(re.escape(frag))

        pat = re.compile(r'\A' + r'\.'.join(pats) + r'\Z', re.IGNORECASE)
        return pat.match(hostname)

    def match_hostname(cert, hostname):
        """Verify that *cert* (in decoded format as returned by
        SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
        rules are followed, but IP addresses are not accepted for *hostname*.

        CertificateError is raised on failure. On success, the function
        returns nothing.
        """
        if not cert:
            raise ValueError("empty or no certificate")
        dnsnames = []
        san = cert.get('subjectAltName', ())
        for key, value in san:
            if key == 'DNS':
                if _dnsname_match(value, hostname):
                    return
                dnsnames.append(value)
        if not dnsnames:
            # The subject is only checked when there is no dNSName entry
            # in subjectAltName
            for sub in cert.get('subject', ()):
                for key, value in sub:
                    # XXX according to RFC 2818, the most specific Common Name
                    # must be used.
                    if key == 'commonName':
                        if _dnsname_match(value, hostname):
                            return
                        dnsnames.append(value)
        if len(dnsnames) > 1:
            raise CertificateError(
                "hostname %r doesn't match either of %s"
                % (hostname, ', '.join(map(repr, dnsnames))))
        elif len(dnsnames) == 1:
            raise CertificateError(
                "hostname %r doesn't match %r"
                % (hostname, dnsnames[0]))
        else:
            raise CertificateError(
                "no appropriate commonName or "
                "subjectAltName fields were found")


class VerifyingHTTPSHandler(HTTPSHandler):
    """Simple verifying handler: no auth, subclasses, timeouts, etc."""

    def __init__(self, ca_bundle):
        self.ca_bundle = ca_bundle
        HTTPSHandler.__init__(self)

    def https_open(self, req):
        return self.do_open(
            lambda host, **kw: VerifyingHTTPSConn(host, self.ca_bundle, **kw),
            req
        )


class VerifyingHTTPSConn(HTTPSConnection):
    """Simple verifying connection: no auth, subclasses, timeouts, etc."""

    def __init__(self, host, ca_bundle, **kw):
        HTTPSConnection.__init__(self, host, **kw)
        self.ca_bundle = ca_bundle

    def connect(self):
        sock = socket.create_connection(
            (self.host, self.port), getattr(self, 'source_address', None)
        )

        # Handle the socket if a (proxy) tunnel is present
        if hasattr(self, '_tunnel') and getattr(self, '_tunnel_host', None):
            self.sock = sock
            self._tunnel()
            # http://bugs.python.org/issue7776: Python>=3.4.1 and >=2.7.7
            # change self.host to mean the proxy server host when tunneling is
            # being used. Adapt, since we are interested in the destination
            # host for the match_hostname() comparison.
            actual_host = self._tunnel_host
        else:
            actual_host = self.host

        if hasattr(ssl, 'create_default_context'):
            ctx = ssl.create_default_context(cafile=self.ca_bundle)
            self.sock = ctx.wrap_socket(sock, server_hostname=actual_host)
        else:
            # This is for python < 2.7.9 and < 3.4?
            self.sock = ssl.wrap_socket(
                sock, cert_reqs=ssl.CERT_REQUIRED, ca_certs=self.ca_bundle
            )
        try:
            match_hostname(self.sock.getpeercert(), actual_host)
        except CertificateError:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            raise


def opener_for(ca_bundle=None):
    """Get a urlopen() replacement that uses ca_bundle for verification"""
    return urllib.request.build_opener(
        VerifyingHTTPSHandler(ca_bundle or find_ca_bundle())
    ).open


# from jaraco.functools
def once(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(func, 'always_returns'):
            func.always_returns = func(*args, **kwargs)
        return func.always_returns
    return wrapper


@once
def get_win_certfile():
    try:
        import wincertstore
    except ImportError:
        return None

    class CertFile(wincertstore.CertFile):
        def __init__(self):
            super(CertFile, self).__init__()
            atexit.register(self.close)

        def close(self):
            try:
                super(CertFile, self).close()
            except OSError:
                pass

    _wincerts = CertFile()
    _wincerts.addstore('CA')
    _wincerts.addstore('ROOT')
    return _wincerts.name


def find_ca_bundle():
    """Return an existing CA bundle path, or None"""
    extant_cert_paths = filter(os.path.isfile, cert_paths)
    return (
        get_win_certfile()
        or next(extant_cert_paths, None)
        or _certifi_where()
    )


def _certifi_where():
    try:
        return __import__('certifi').where()
    except (ImportError, ResolutionError, ExtractionError):
        pass
