
'''
Bidirectional search is a graph search algorithm which find smallest path form source to goal vertex. It runs two simultaneous search –

Forward search form source/initial vertex toward goal vertex
Backward search form goal/target vertex toward source vertex
Bidirectional search replaces single search graph(which is likely to grow exponentially) with two smaller sub graphs – one starting from initial vertex and other starting from goal vertex. The search terminates when two graphs intersect.
'''




class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        n = len(stones)
        if n < 2: return True
        if stones[1] != 1: return False
        if n == 2: return True

        set_stones = set(stones)
        set_forward, set_backward = set([(1, 1)]), set()
        que_forward, que_backward = deque([(1, 1)]), deque()

        for i in range(n-2, 0, -1):
            temp = ((stones[-1], stones[-1]-stones[i]))
            set_backward.add(temp)
            que_backward.append(temp)

        while que_forward and que_backward:
            pos, jump = que_forward.popleft()
            # print('forward', (pos, jump))
            for i in range(1, -2, -1):
                if pos + jump + i in set_stones:
                    if jump + i <= 0: continue
                    status = (pos + jump + i, jump + i)
                    if status in set_forward: continue
                    if status in set_backward:
                        return True
                    set_forward.add(status)
                    que_forward.append(status)


            pos, jump = que_backward.popleft()
            # print('backward', (pos, jump))
            for i in range(1, -2, -1):
                if pos - (jump + i) in set_stones:
                    if jump + i <= 0: continue
                    status = (pos - jump - i, jump + i)
                    if status in set_backward: continue
                    if status in set_forward:
                        return True
                    set_backward.add(status)
                    que_backward.append(status)

        return False
