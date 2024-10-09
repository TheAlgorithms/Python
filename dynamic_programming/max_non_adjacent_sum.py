# Video Açıklaması: https://www.youtube.com/watch?v=6w60Zi1NtL8&feature=emb_logo

from __future__ import annotations


def maksimum_non_ardisik_toplam(nums: list[int]) -> int:
    """
    nums giriş listesindeki tamsayıların maksimum ardışık olmayan toplamını bulun

    >>> maksimum_non_ardisik_toplam([1, 2, 3])
    4
    >>> maksimum_non_ardisik_toplam([1, 5, 3, 7, 2, 2, 6])
    18
    >>> maksimum_non_ardisik_toplam([-1, -5, -3, -7, -2, -2, -6])
    0
    >>> maksimum_non_ardisik_toplam([499, 500, -3, -7, -2, -2, -6])
    500
    """
    if not nums:
        return 0
    max_dahil = nums[0]
    max_haric = 0
    for num in nums[1:]:
        max_dahil, max_haric = (
            max_haric + num,
            max(max_dahil, max_haric),
        )
    return max(max_haric, max_dahil)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
