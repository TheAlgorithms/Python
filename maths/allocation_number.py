from __future__ import annotations


def allocation_num(number_of_bytes: int, partitions: int) -> list[str]:
    """
    Divide a number of bytes into x partitions.

    In a multi-threaded download, this algorithm could be used to provide
    each worker thread with a block of non-overlapping bytes to download.
    For example:
        for i in allocation_list:
            requests.get(url,headers={'Range':f'bytes={i}'})

    parameter
    ------------
    : param number_of_bytes
    : param partitions

    return
    ------------
    : return: list of bytes to be assigned to each worker thread

    Examples:
    ------------
    >>> allocation_num(16647, 4)
    ['0-4161', '4162-8322', '8323-12483', '12484-16647']
    >>> allocation_num(888, 888)
    Traceback (most recent call last):
        ...
    ValueError: partitions can not >= number_of_bytes!
    >>> allocation_num(888, 999)
    Traceback (most recent call last):
        ...
    ValueError: partitions can not >= number_of_bytes!
    >>> allocation_num(888, -4)
    Traceback (most recent call last):
        ...
    ValueError: partitions must be a positive number!
    """
    if partitions <= 0:
        raise ValueError("partitions must be a positive number!")
    if partitions >= number_of_bytes:
        raise ValueError("partitions can not >= number_of_bytes!")
    bytes_per_partition = number_of_bytes // partitions
    allocation_list = [f"0-{bytes_per_partition}"]
    for i in range(1, partitions - 1):
        length = f"{bytes_per_partition * i + 1}-{bytes_per_partition * (i + 1)}"
        allocation_list.append(length)
    allocation_list.append(
        f"{(bytes_per_partition * (partitions - 1)) + 1}-" f"{number_of_bytes}"
    )
    return allocation_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
