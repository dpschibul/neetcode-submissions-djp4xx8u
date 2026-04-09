class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = 0

        for pos in range(len(heights)):
            maximum = max(maximum, self.checkMaxForPos(heights, pos))
        return maximum
        

    def checkMaxForPos(self, heights: List[int], pos: int) -> int:
                left = pos-1
                width = 1
                while left >= 0 and heights[left] >= heights[pos]:
                    left-=1
                    width+=1

                right = pos+1
                while right < len(heights) and heights[right] >= heights[pos]:
                    right+=1
                    width+=1

                return heights[pos] * width






