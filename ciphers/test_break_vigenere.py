import math

from ciphers.break_vigenere import (
    LETTER_FREQUENCIES_DICT,
    calculate_indexes_of_coincidence,
    find_key,
    find_key_from_vigenere_cipher,
    friedman_method,
    get_frequencies,
    index_of_coincidence,
)


class Test:
    def test_index_of_coincidence(self):
        ic = index_of_coincidence({"a": 50, "b": 50}, 50)
        assert math.isclose(ic, 2.0)

    def test_calculate_indexes_of_coincidence(self):
        ciphertext = "hellothere"
        result = calculate_indexes_of_coincidence(ciphertext, 2)
        assert result == [0.1, 0.3]

    def test_friedman_method(self):
        ciphertext = "asqsfdybpypvhftnboexqumfsnglmcstyefv".upper()
        result = friedman_method(ciphertext, 5)
        assert result == 3

    def test_get_frequencies(self):
        result = get_frequencies()
        expected = tuple(num / 100 for num in LETTER_FREQUENCIES_DICT.values())
        assert result == expected

    def test_find_key(self):
        ciphertext = "asqsfdybpypvhftnboexqumfsnglmcstyefv".upper()
        result = find_key(ciphertext, 3)
        assert result == "ABC"

    def test_find_key_from_vigenere_cipher(self):
        ciphertext = (
            "A dqxryeocqgj mpth ms sptusb ticq ms aoihv. Fgf "
            "edrsou ylxmes jhv, sos exwyon uweqe igu msfjplxj "
            "vbtliyy. Bno xme xqupi's b uwele, bpg eql ujh qjn bpg "
            "atmfp piwema spfyftv. E wotg ec fnz qwljr ocpi bovng "
            "wremn dw xwfgw."
        )
        result = find_key_from_vigenere_cipher(ciphertext)
        assert result == "ABCDEF"
