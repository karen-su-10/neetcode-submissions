class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash_set = set()
        l =0
        max_len =0
        for r in range(len(s)):
            right_val = s[r]
             #shrink the window
            while right_val in hash_set:
                hash_set.remove(s[l])
                l +=1
            hash_set.add(right_val)
            max_len =max(max_len, r-l+1)
        return max_len

            
