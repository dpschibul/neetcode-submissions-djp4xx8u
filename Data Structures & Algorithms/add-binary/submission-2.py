class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = ""
        carry = False
        while i >= 0 and j >= 0:
            if a[i] == "1" and b[j] == "1" and carry:
                res = "1" + res
            elif a[i] == "1" and b[j] == "1" or ((a[i] == "1" or b[j] == "1") and carry):
                res = "0" + res
                carry = True
            elif a[i] == "1" or b[j] == "1" or carry:
                res = "1" + res
                carry = False
            else:
                res = "0" + res
                carry = False
            i -= 1
            j -= 1
        
        while i >= 0:
            if carry and a[i] == "1":
                res = "0" + res
            elif a[i] == "1" or carry:
                res = "1" + res
                carry = False
            else:
                res = "0" + res
                carry = False
            i -= 1
        
        while j >= 0:
            if carry and b[j]  == "1":
                res = "0" + res
            elif b[j] == "1" or carry:
                res = "1" + res
                carry = False
            else:
                res = "0" + res
                carry = False
            j -= 1
        
        if carry:
            res = "1" + res
        return res
        
        
        