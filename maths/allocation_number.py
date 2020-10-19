"""
In a multi-threaded download, this algorithm could be used to provide
each worker thread with a block of non-overlapping bytes to download.
For example:
    for i in allocation_list:
        requests.get(url,headers={'Range':f'bytes={i}'})
"""
from __future__ import annotations


def allocation_num(number_of_bytes: int, partitions: int) -> list[str]:
    """
    Divide a number of bytes into x partitions.
    :param number_of_bytes: the total of bytes.
    :param partitions: the number of partition need to be allocated.
    :return: list of bytes to be assigned to each worker thread

    >>> allocation_num(16647, 4)
    ['1-4161', '4162-8322', '8323-12483', '12484-16647']
    >>> allocation_num(50000, 5)
    ['1-10000', '10001-20000', '20001-30000', '30001-40000', '40001-50000']
    >>> allocation_num(888, 999)
    Traceback (most recent call last):
        ...
    ValueError: partitions can not > number_of_bytes!
    >>> allocation_num(888, -4)
    Traceback (most recent call last):
        ...
    ValueError: partitions must be a positive number!
    """
    if partitions <= 0:
        raise ValueError("partitions must be a positive number!")
    if partitions > number_of_bytes:
        raise ValueError("partitions can not > number_of_bytes!")
    bytes_per_partition = number_of_bytes // partitions
    allocation_list = []
    for i in range(partitions):
        start_bytes = i * bytes_per_partition + 1
        end_bytes = (
            number_of_bytes if i == partitions - 1 else (i + 1) * bytes_per_partition
        )
        allocation_list.append(f"{start_bytes}-{end_bytes}")
    return allocation_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
