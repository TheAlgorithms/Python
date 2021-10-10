def uniqueness(string: str):
    if(set(string)==len(string)):
        return string+" - CONTAINS ALL UNIQUE CHARACTERS"
    else:
        return string+" - DOSEN'T CONTAINS UNIQUE CHARACTERS"
    return None