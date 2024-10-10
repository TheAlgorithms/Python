"""
LZ77 sıkıştırma algoritması
- 1977 yılında Abraham Lempel ve Jacob Ziv tarafından yayımlanan kayıpsız veri sıkıştırma
- LZ1 veya kaydırmalı pencere sıkıştırması olarak da bilinir
- LZW, LZSS, LZMA ve diğer birçok varyasyonun temelini oluşturur

Bu algoritma “kaydırmalı pencere” yöntemini kullanır. Kaydırmalı pencerede şunlar bulunur:
  - arama tamponu
  - ileri bakış tamponu
len(kaydırmalı_pencere) = len(arama_tamponu) + len(ileri_bakış_tamponu)

LZ77, üçlülerden oluşan bir sözlük yönetir:
    - Arama tamponundaki ofset, bir ifadenin başlangıcı ile dosyanın başlangıcı arasındaki mesafedir.
    - Eşleşme uzunluğu, bir ifadeyi oluşturan karakter sayısını belirtir.
    - Göstergesi, bir sonraki kodlanacak karakteri temsil eden bir karakterdir.

Bir dosya ayrıştırıldıkça, sözlük dinamik olarak güncellenir ve sıkıştırılmış veri içeriği ve boyutunu yansıtır.

Örnekler:
"cabracadabrarrarrad" <-> [(0, 0, 'c'), (0, 0, 'a'), (0, 0, 'b'), (0, 0, 'r'),
                           (3, 1, 'c'), (2, 1, 'd'), (7, 4, 'r'), (3, 5, 'd')]
"ababcbababaa" <-> [(0, 0, 'a'), (0, 0, 'b'), (2, 2, 'c'), (4, 3, 'a'), (2, 2, 'a')]
"aacaacabcabaaac" <-> [(0, 0, 'a'), (1, 1, 'c'), (3, 4, 'b'), (3, 3, 'a'), (1, 2, 'c')]

Kaynaklar:
en.wikipedia.org/wiki/LZ77_and_LZ78
"""

from dataclasses import dataclass

__version__ = "0.1"
__author__ = "Lucia Harcekova"


@dataclass
class Token:
    """
    Uzunluk, ofset ve gösterge içeren üçlü olarak adlandırılan token'ı temsil eden veri sınıfı.
    Bu üçlü, LZ77 sıkıştırması sırasında kullanılır.
    """

    offset: int
    length: int
    indicator: str

    def __repr__(self) -> str:
        """
        >>> token = Token(1, 2, "c")
        >>> repr(token)
        '(1, 2, c)'
        >>> str(token)
        '(1, 2, c)'
        """
        return f"({self.offset}, {self.length}, {self.indicator})"


class LZ77Compressor:
    """
    LZ77 sıkıştırma algoritmasını kullanarak sıkıştırma ve açma yöntemlerini içeren sınıf.
    """

    def __init__(self, window_size: int = 13, lookahead_buffer_size: int = 6) -> None:
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size
        self.search_buffer_size = self.window_size - self.lookahead_buffer_size

    def compress(self, text: str) -> list[Token]:
        """
        Verilen metin dizesini LZ77 sıkıştırma algoritması kullanarak sıkıştırır.

        Args:
            text: sıkıştırılacak dize

        Returns:
            output: sıkıştırılmış metin, Token'ların bir listesi olarak

        >>> lz77_compressor = LZ77Compressor()
        >>> str(lz77_compressor.compress("ababcbababaa"))
        '[(0, 0, a), (0, 0, b), (2, 2, c), (4, 3, a), (2, 2, a)]'
        >>> str(lz77_compressor.compress("aacaacabcabaaac"))
        '[(0, 0, a), (1, 1, c), (3, 4, b), (3, 3, a), (1, 2, c)]'
        """

        output = []
        search_buffer = ""

        # Sıkıştırılacak metinde hala karakterler varken
        while text:
            # Bir sonraki kodlama ifadesini bul
            # - ofset, uzunluk, gösterge ile üçlü
            token = self._find_encoding_token(text, search_buffer)

            # Arama tamponunu güncelle:
            # - metinden yeni karakterler ekle
            # - boyut maksimum arama tamponu boyutunu aşarsa, en eski elemanları çıkar
            search_buffer += text[: token.length + 1]
            if len(search_buffer) > self.search_buffer_size:
                search_buffer = search_buffer[-self.search_buffer_size :]

            # Metni güncelle
            text = text[token.length + 1 :]

            # Token'ı çıktıya ekle
            output.append(token)

        return output

    def decompress(self, tokens: list[Token]) -> str:
        """
        Token listesini bir çıktı dizesine dönüştürür.

        Args:
            tokens: üçlüleri (ofset, uzunluk, char) içeren liste

        Returns:
            output: açılmış metin

        Testler:
            >>> lz77_compressor = LZ77Compressor()
            >>> lz77_compressor.decompress([Token(0, 0, 'c'), Token(0, 0, 'a'),
            ... Token(0, 0, 'b'), Token(0, 0, 'r'), Token(3, 1, 'c'),
            ... Token(2, 1, 'd'), Token(7, 4, 'r'), Token(3, 5, 'd')])
            'cabracadabrarrarrad'
            >>> lz77_compressor.decompress([Token(0, 0, 'a'), Token(0, 0, 'b'),
            ... Token(2, 2, 'c'), Token(4, 3, 'a'), Token(2, 2, 'a')])
            'ababcbababaa'
            >>> lz77_compressor.decompress([Token(0, 0, 'a'), Token(1, 1, 'c'),
            ... Token(3, 4, 'b'), Token(3, 3, 'a'), Token(1, 2, 'c')])
            'aacaacabcabaaac'
        """

        output = ""

        for token in tokens:
            for _ in range(token.length):
                output += output[-token.offset]
            output += token.indicator

        return output

    def _find_encoding_token(self, text: str, search_buffer: str) -> Token:
        """Metindeki ilk karakter için kodlama token'ını bulur.

        Testler:
            >>> lz77_compressor = LZ77Compressor()
            >>> lz77_compressor._find_encoding_token("abrarrarrad", "abracad").offset
            7
            >>> lz77_compressor._find_encoding_token("adabrarrarrad", "cabrac").length
            1
            >>> lz77_compressor._find_encoding_token("abc", "xyz").offset
            0
            >>> lz77_compressor._find_encoding_token("", "xyz").offset
            Traceback (most recent call last):
                ...
            ValueError: Çalışmak için biraz metne ihtiyacımız var.
            >>> lz77_compressor._find_encoding_token("abc", "").offset
            0
        """

        if not text:
            raise ValueError("Çalışmak için biraz metne ihtiyacımız var.")

        # Sonuç parametrelerini varsayılan değerlere başlat
        length, offset = 0, 0

        if not search_buffer:
            return Token(offset, length, text[length])

        for i, character in enumerate(search_buffer):
            found_offset = len(search_buffer) - i
            if character == text[0]:
                found_length = self._match_length_from_index(text, search_buffer, 0, i)
                # Bulunan uzunluk mevcut olandan büyükse veya eşitse,
                # bu durumda ofset daha küçük: ofset ve uzunluğu güncelle
                if found_length >= length:
                    offset, length = found_offset, found_length

        return Token(offset, length, text[length])

    def _match_length_from_index(
        self, text: str, window: str, text_index: int, window_index: int
    ) -> int:
        """Metin ve pencere karakterlerinin en uzun eşleşmesini hesaplar
        text_index ve window_index'ten itibaren.

        Args:
            text: _açıklama_
            window: kaydırmalı pencere
            text_index: metindeki karakterin indeksi
            window_index: kaydırmalı penceredeki karakterin indeksi

        Returns:
            Verilen indekslerden metin ve pencere arasındaki maksimum eşleşme.

        Testler:
            >>> lz77_compressor = LZ77Compressor(13, 6)
            >>> lz77_compressor._match_length_from_index("rarrad", "adabrar", 0, 4)
            5
            >>> lz77_compressor._match_length_from_index("adabrarrarrad",
            ...     "cabrac", 0, 1)
            1
        """
        if not text or text[text_index] != window[window_index]:
            return 0
        return 1 + self._match_length_from_index(
            text, window + text[text_index], text_index + 1, window_index + 1
        )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # Sıkıştırıcı sınıfını başlat
    lz77_compressor = LZ77Compressor(window_size=13, lookahead_buffer_size=6)

    # Örnek
    TEXT = "cabracadabrarrarrad"
    compressed_text = lz77_compressor.compress(TEXT)
    print(lz77_compressor.compress("ababcbababaa"))
    decompressed_text = lz77_compressor.decompress(compressed_text)
    assert decompressed_text == TEXT, "LZ77 algoritması geçersiz bir sonuç döndürdü."
