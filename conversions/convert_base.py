def micro_convert(n, base1, base2):
    converted = 0
    multiplier = 1
    while n:
        converted += (n % base2) * multiplier
        multiplier *= base1
        n = n // base2
    return converted


def convert_base(num, frombase, tobase):
    return micro_convert(micro_convert(num, frombase, 10), 10, tobase)
