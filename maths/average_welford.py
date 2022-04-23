def average_welford(values: list) -> float:
    """
      >>> average_welford([1, 2, 3, 4, 5])
      3.0
      >>> average_welford([1.2329435, 2.209462409, 3.230925, 4.47626462, 5.2938759204])
      3.2886942898799996
      >>> average_welford([-57386462.2329435, 2246262.209462409, 4632463.230925, 856737354.47626462, -243664265.2938759204])
      112513070.4779665
    """
    avg = 0.0
    """while looping through the list,
       we calculate the average of the
       current element and the average
       of the elements before it"""
    for index in range(0, len(values)):
      avg += (values[index]-avg)/(index+1)
    return avg

if __name__ == "__main__":
      import doctest
      doctest.testmod()
