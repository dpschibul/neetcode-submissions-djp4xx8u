class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)

        if "0000" in ends:
            return -1
        
        q = deque(["0000"])
        steps = 0
        visit = set(deadends)

        while q:
            q_length = len(q)
            for i in range(q_length):
                val = q.popleft()
                if val == target:
                    return steps

                for i in range(4):
                    plus = (int(val[i]) + 1) % 10
                    minus = (int(val[i]) - 1 + 10) % 10
                    val1 = val[:i] + str(plus) + val[i+1:]
                    val2 = val[:i] + str(minus) + val[i+1:]
                    if val1 not in visit:
                        visit.add(val1)
                        q.append(val1)
                    if val2 not in visit:
                        visit.add(val2)
                        q.append(val2)

            steps += 1

        return -1

        

