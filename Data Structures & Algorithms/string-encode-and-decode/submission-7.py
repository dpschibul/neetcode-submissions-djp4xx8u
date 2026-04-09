class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        l, r = 0,0
        le=""
        while r < len(s):
            while s[r] != "#":
                le+=s[r]
                r+=1
            print(le)
            length=int(le)
            res.append(s[r+1:r+length+1])
            r+=length+1
            le=""

        return res
            
            