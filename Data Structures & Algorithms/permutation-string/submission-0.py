class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        target = Counter(s1)
        window = Counter(s2[:m])

        if window==target:
            return True
        
        for right in range(m,n):
            window[s2[right]]+=1
            outgoing = s2[right-m]
            window[outgoing]-=1

            if window[outgoing] ==0:
                del window[outgoing]
            if window == target:
                return True
        
        return False
        