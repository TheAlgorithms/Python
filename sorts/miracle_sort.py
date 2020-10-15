# From https://github.com/Seluj78/MiracleSort

def _is_sorted(lst: list) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def miraclesort(lst: list) -> list:
    while not _is_sorted(lst):
        pass
    return lst
