class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(n + 1):
            cur = i
            count = 0
            while cur > 0:
                if cur & 1 == 1:
                    count += 1
                cur >>= 1
            res.append(count)
        return res


        