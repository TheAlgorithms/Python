"""
    This is a simple implementation of SSTF algorithm to calculate total time.

"""

print("Enter the requests separated by ' ' :-")
req = list(map(int, input().split(" ")))
head = int(input("Enter the head of the pointer :-"))
req.append(head)
req.sort()
t_time = 0

while len(req) != 0:
    if req.index(head) != 0 or req.index(head) != len(req) - 1:
        curr_index = req.index(head)
        prev = abs(req[curr_index - 1] - head)
        nxt = abs(req[curr_index + 1] - head)

        if prev < nxt:
            t_time += prev
            head = req[curr_index - 1]
            req.pop(curr_index)
        if nxt <= prev:
            t_time += nxt
            head = req[curr_index + 1]
            req.pop(curr_index)
    elif req.index(head) == 0:
        try:
            t_time += abs(req[curr_index + 1] - head)
            head = req[curr_index + 1]
            req.pop(curr_index)
            t_time += abs(req[1] - head)
            head = req[1]
            req.pop(0)
        except:
            break
    elif req.index(head) == len(req) - 1:
        t_time += abs(req[len(req) - 2] - head)
        head = req[len(req) - 2]
        req.pop(len(req) - 1)
    else:
        pass

print("total time is", t_time)
