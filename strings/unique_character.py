def uniqueness(string: str):
    if(len(set(string))==len(string)):
        return string+" - CONTAINS ALL UNIQUE CHARACTERS"
    else:
        return string+" - DOSEN'T CONTAINS UNIQUE CHARACTERS"
    return None