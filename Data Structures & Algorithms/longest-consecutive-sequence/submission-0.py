class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #each check is O(1)
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            #find the beginning of the sequence, set as the current_num, current_length
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                # find the continued sequence number and add on the current_length
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                #swap the max length if needed
                max_length = max(max_length, current_length)
        return max_length