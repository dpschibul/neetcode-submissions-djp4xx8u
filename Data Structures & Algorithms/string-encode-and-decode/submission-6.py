class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out = out + str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
    
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            res.append(s[i + 1: i + 1 + length])
            i = i + 1 + length


        return res
            

