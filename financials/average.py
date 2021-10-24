def weighted(ratio,rates):
    result = 0
    for index in range(len(ratio)):
        result = result + ratio[index]*rates[index]
    return result
