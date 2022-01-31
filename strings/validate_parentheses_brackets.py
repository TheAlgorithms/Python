def isValid(self, s: str) -> bool:
    stack: list = []
    dic: dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for ch in s:
        if ch in dic:
            x = stack.pop()
            if dic[ch] != x:
                return False
        stack.append(ch)
    
    return True