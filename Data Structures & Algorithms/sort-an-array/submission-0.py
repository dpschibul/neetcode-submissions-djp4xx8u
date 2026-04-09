class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            sortedLeft = mergesort(left)
            sortedRight = mergesort(right)

            return merge(sortedLeft, sortedRight)
        
        def merge(left, right):
            res = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res.extend(left[i:])
            res.extend(right[j:])
            return res

        return mergesort(nums)

            
        