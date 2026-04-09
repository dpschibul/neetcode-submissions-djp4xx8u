class Solution:
    def reverseBits(self, n: int) -> int:
        rev = ""
        while n > 0:
            if n & 1:
                rev += "1"
            else:
                rev += "0"
            n >>= 1

        while len(rev) < 32:
            rev += "0"
        return int(rev, 2)
        