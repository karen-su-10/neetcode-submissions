class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        required = len(need)
        formed = 0

        left = 0
        best_len = float('inf')
        best_start = 0

        for right in range(len(s)):
            c = s[right]

            # TODO 1: update window frequency
            window[c] = window.get(c,0)+1

            # TODO 2: update formed when threshold reached
            if c in need and window[c]==need[c]:
                formed +=1

            # TODO 3: shrink while valid
            #   a. update best_len / best_start
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
            #   b. remove outgoing character
                outgoing = s[left]
                window[outgoing]-=1
            #   c. update formed if threshold broken
                if outgoing in need and window[outgoing]<need[outgoing]:
                  formed-=1
            #   d. advance left
                left+=1

        if best_len == float('inf'):
            return ""

        return s[best_start:best_start + best_len]