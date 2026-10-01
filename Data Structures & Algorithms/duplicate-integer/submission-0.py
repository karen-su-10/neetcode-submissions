class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #new hashmap/dict, the number as key
        key_map = dict()
        #loop through, if key exist, return true.
        for i in nums:
            if i not in key_map:
                key_map[i] = True
            else:
                return True

        #until the end, return false
        return False
        #time O(n)*O(1) = O(n), space O(n)
        