class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            if stack and heights[stack[-1]] < heights[i]:
                stack.append(i)
        return stack[::-1]

