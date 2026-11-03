class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        target = Counter(s1)
        window = Counter(s2[:m])
        # dict1 == dict2 比较内容，不比较顺序；普通 dict 不会忽略零值 key。
        # target = {}
        # window = {}

        # # Step 1: Build target frequency
        # for char in s1:
        #     target[char] = target.get(char, 0) + 1

        # # Step 2: Initialize first window
        # for char in s2[:m]:
        #     window[char] = window.get(char, 0) + 1
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
        