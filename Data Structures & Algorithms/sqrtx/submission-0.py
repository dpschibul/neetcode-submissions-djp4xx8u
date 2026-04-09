class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = (l + r )// 2
            sqrt = mid*mid

            if sqrt == x:
                return mid
            if sqrt < x:
                l = mid+1
            else:
                r = mid-1
        return r
            

        