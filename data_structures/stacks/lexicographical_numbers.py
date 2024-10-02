def lexical_order(n: int) -> str:

    ans = []
    stack = [1]

    while stack:
        num = stack.pop()
        if num > n:
            continue
        
        ans.append(str(num))
        if (num % 10) != 9:  
            stack.append(num + 1)

        stack.append(num * 10)

    return " ".join(ans)

if __name__ == "__main__":

    print(f"Numbers from 1 to 25 in lexical order: {lexical_order(25)}")
