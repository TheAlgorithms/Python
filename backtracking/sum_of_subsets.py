"""
Alt kümelerin toplamı problemi, negatif olmayan tamsayılar kümesi ve bir M değeri verildiğinde,
verilen kümenin toplamı verilen M'ye eşit olan tüm olası alt kümelerini belirler.

Seçilen sayıların toplamı verilen M sayısına eşit olmalıdır ve bir sayı yalnızca bir kez kullanılabilir.
"""

from __future__ import annotations


def alt_kümelerin_toplamını_üret(nums: list[int], max_sum: int) -> list[list[int]]:
    sonuç: list[list[int]] = []
    yol: list[int] = []
    sayı_indeksi = 0
    kalan_sayılar_toplamı = sum(nums)
    durum_uzayı_ağacı_oluştur(nums, max_sum, sayı_indeksi, yol, sonuç, kalan_sayılar_toplamı)
    return sonuç


def durum_uzayı_ağacı_oluştur(
    nums: list[int],
    max_sum: int,
    sayı_indeksi: int,
    yol: list[int],
    sonuç: list[list[int]],
    kalan_sayılar_toplamı: int,
) -> None:
    """
    DFS kullanarak her dalı yinelemek için bir durum uzayı ağacı oluşturur.
    Aşağıdaki iki koşuldan herhangi biri sağlandığında bir düğümün dallanmasını sonlandırır.
    Bu algoritma derinlik öncelikli arama (DFS) izler ve düğüm dallanabilir olmadığında geri izler.

    """
    if sum(yol) > max_sum or (kalan_sayılar_toplamı + sum(yol)) < max_sum:
        return
    if sum(yol) == max_sum:
        sonuç.append(yol)
        return
    for index in range(sayı_indeksi, len(nums)):
        durum_uzayı_ağacı_oluştur(
            nums,
            max_sum,
            index + 1,
            [*yol, nums[index]],
            sonuç,
            kalan_sayılar_toplamı - nums[index],
        )


"""
Kullanıcıdan girdi almak için yorumu kaldırın

print("Elemanları girin")
nums = list(map(int, input().split()))
print("Maksimum toplamı girin")
max_sum = int(input())

"""
nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
sonuç = alt_kümelerin_toplamını_üret(nums, max_sum)
print(*sonuç)
