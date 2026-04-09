class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.count = defaultdict(int)
        self.freq = defaultdict(list)

        

    def push(self, val: int) -> None:
        self.count[val]+=1
        self.max_freq = max(self.max_freq, self.count[val])
        self.freq[self.count[val]].append(val)

    def pop(self) -> int:
        val = self.freq[self.max_freq].pop()
        self.count[val] -= 1
        if not self.freq[self.max_freq]:
            self.max_freq -= 1
        return val

        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# [5, 4, 5, 3, 4, 2, 5]
#  { 2: [5, 3]}
#  max = 2 pop { 1: [3], 2: [5]}