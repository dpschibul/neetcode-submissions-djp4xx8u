class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []

        for i, h in enumerate(height):
            if i == 0:
                leftMax.append(0)
            else:
                leftMax.append(max(height[i - 1], leftMax[-1]))

        for i, h in enumerate(height[::-1]):
            if i == 0:
                rightMax.append(0)
            else:
                rightMax.append(max(height[::-1][i - 1], rightMax[-1]))
        
        out = 0

        for i, h in enumerate(height):
            out += max(0, min(leftMax[i], rightMax[::-1][i]) - h)

        return out


       
        