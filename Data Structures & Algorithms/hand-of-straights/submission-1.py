class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,4,2,3,5,3,4], groupSize = 4
        #  visit = set() if index in res: continue
        if len(hand) % groupSize != 0:
            return False
        visit = set()
        hand.sort()

        while len(visit) < len(hand) and len(visit) % groupSize == 0:
            cur = -1

            for i, h in enumerate(hand):
                if i in visit:
                    continue
                if cur == -1:
                    cur = h
                    visit.add(i)
                    continue
                if cur == h-1:
                    visit.add(i)
                    cur = h

                if len(visit) % groupSize == 0:
                    break

        return len(visit) == len(hand) 

        