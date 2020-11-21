def ohms_law(v=0, i=0, r=0):
    if v == 0:
        result = (i*r)
        return result
    elif i == 0:
        result = (v/r)
        return result
    elif r == 0:
        result = (v/r)
        return result
    else:
        return 0
