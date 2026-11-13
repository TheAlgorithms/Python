import pytest

from ciphers.des_ecb import Des


@pytest.mark.parametrize(
    "text",
    [
        "Hello",
        "Hello \u20ac",
        "\u65e5\u672c\u8a9e",
        "r\u00e9sum\u00e9",
        "Hello \u20ac!",
        "\U0001f600",
        "1234567\u20ac",
        "abc\x00def",
    ],
)
def test_des_unicode_round_trip(text: str) -> None:
    key = "133457799BBCDFF1"
    encrypted = Des.encrypt(key, text)
    decrypted = Des.decrypt(key, encrypted)

    assert decrypted == text
