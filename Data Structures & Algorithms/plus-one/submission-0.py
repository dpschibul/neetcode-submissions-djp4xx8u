class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            num = digits[i] + 1 
            if digits[i] + 1 <= 9:
                digits[i] = num
                return digits
            
            digits[i] = num % 10
        
        if digits[0] == 0:
            temp = [1]
            temp.extend(digits)
            return temp
        return digits

        