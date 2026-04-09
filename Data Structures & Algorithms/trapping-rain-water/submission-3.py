class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        out = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                out += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(height[r], rightMax)
                out += rightMax - height[r]
        return out


       
        