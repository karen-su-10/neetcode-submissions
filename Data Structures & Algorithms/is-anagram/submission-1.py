class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        # Count characters in s
        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1

        # Count characters in t
        for j in t:
            dic_t[j] = dic_t.get(j, 0) + 1

        # Compare counts
        for i in dic_s:
            if dic_t.get(i, 0) != dic_s[i]:
                return False

        return True

        #Space O(n)+ O(n) = O(n); Time O(n)