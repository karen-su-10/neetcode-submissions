class Solution:
    def isPalindrome(self, s: str) -> bool:
        #loop through this string, create two arrays
        array_forward =[]
        for c in s:
            if c.isalnum():
                array_forward.append(c.lower())
        #reverse the array:
        array_backward =[]
        for i in range(len(array_forward)-1,-1,-1):
            array_backward.append(array_forward[i])

        # go through both
        for i in range(0, len(array_forward)):
            if array_forward[i]!=array_backward[i]:
                return False
        
        return True