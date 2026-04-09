class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length()-1

        peak = -1

        while left <= right:
            mid = left + (right - left) // 2

            val = mountainArr.get(mid) 
            low = mountainArr.get(mid-1) 
            high = mountainArr.get(mid+1)

            if low < val and high < val:
                peak = mid
            
            if low < val < high:
                left = mid+1
            else:
                right = mid-1
            
        left, right = 0, peak

        while left <= right:
            mid = left + (right - left) // 2

            val = mountainArr.get(mid)

            if val == target:
                return mid
            
            if val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left, right = peak+1, mountainArr.length()-1

        while left <= right:
            mid = left + (right - left) // 2

            val = mountainArr.get(mid)

            if val == target:
                return mid
            
            if val > target:
                left = mid + 1
            else:
                right = mid - 1     
        
        return -1
        