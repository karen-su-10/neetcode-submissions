class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through the array get nums[i], and expected_num = target-nums[i]
        for i in range(0, len(nums)):
            expected_num = target-nums[i]
         #   then for the range from i+1 to len(nums), check if nums[j] == expected_num if so return i and j
            for j in range(i+1, len(nums)):
                if nums[j] == expected_num:
                    return [i, j]
        return [0,0]

        