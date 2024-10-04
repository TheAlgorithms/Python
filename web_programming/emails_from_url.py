"""URL'den site e-postalarını alın."""

from __future__ import annotations

__author__ = "K. Umut Araz"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "K. Umut Araz"
__email__ = "umutaraz349@gmail.com"
__status__ = "Sigma"

import re
from html.parser import HTMLParser
from urllib import parse

import requests


class Parser(HTMLParser):
    def __init__(self, domain: str) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.domain = domain

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """
        Bu fonksiyon, etiketlerden URL'leri almak için HTML'yi ayrıştırır.
        """
        # Sadece 'anchor' etiketini ayrıştır.
        if tag == "a":
            # Tanımlanmış özniteliklerin listesini kontrol et.
            for name, value in attrs:
                # Eğer href tanımlanmışsa, boş değilse ve # değilse ve zaten URL'lerde yoksa.
                if name == "href" and value not in (*self.urls, "", "#"):
                    url = parse.urljoin(self.domain, value)
                    self.urls.append(url)


# Ana domain adını al (example.com)
def get_domain_name(url: str) -> str:
    """
    Bu fonksiyon ana domain adını alır

    >>> get_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'c.d'
    >>> get_domain_name("URL değil!")
    ''
    """
    return ".".join(get_sub_domain_name(url).split(".")[-2:])


# Alt domain adını al (sub.example.com)
def get_sub_domain_name(url: str) -> str:
    """
    >>> get_sub_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'a.b.c.d'
    >>> get_sub_domain_name("URL değil!")
    ''
    """
    return parse.urlparse(url).netloc


def emails_from_url(url: str = "https://github.com") -> list[str]:
    """
    Bu fonksiyon URL alır ve tüm geçerli e-postaları döndürür
    """
    # URL'den ana domaini al
    domain = get_domain_name(url)

    # Ayrıştırıcıyı başlat
    parser = Parser(domain)

    try:
        # URL'yi aç
        r = requests.get(url, timeout=10)

        # Ham HTML'yi ayrıştırıcıya geçirerek bağlantıları al
        parser.feed(r.text)

        # Bağlantıları al ve döngüye gir
        valid_emails = set()
        for link in parser.urls:
            # URL'yi aç.
            try:
                read = requests.get(link, timeout=10)
                # Geçerli e-postayı al.
                emails = re.findall("[a-zA-Z0-9]+@" + domain, read.text)
                # Listede yoksa ekle.
                for email in emails:
                    valid_emails.add(email)
            except ValueError:
                pass
    except ValueError:
        raise SystemExit(1)

    # Son olarak, yinelenen olmadan e-posta adreslerinin sıralanmış bir listesini döndür.
    return sorted(valid_emails)


if __name__ == "__main__":
    emails = emails_from_url("https://github.com")
    print(f"{len(emails)} e-posta bulundu:")
    print("\n".join(sorted(emails)))
