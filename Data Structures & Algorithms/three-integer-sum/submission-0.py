class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the nums list
        sorted_nums = sorted(nums)
        # use two pointers
        res_array = []
        for i in range(len(sorted_nums) - 2):
            #skip duplicates 
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            #two pointers
            target = -sorted_nums[i]
            p1 = i + 1
            p2 = len(sorted_nums) - 1
            while p1 < p2:
                current_sum = sorted_nums[p1] + sorted_nums[p2]
                if current_sum < target:
                    p1 += 1
                elif current_sum > target:
                    p2 -= 1
                else:
                    res_array.append([sorted_nums[i], sorted_nums[p1], sorted_nums[p2]])
                    #update pointers
                    p1 += 1
                    p2 -= 1
                    #skip duplicates
                    while p1 < p2 and sorted_nums[p1] == sorted_nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and sorted_nums[p2] == sorted_nums[p2 + 1]:
                        p2 -= 1
        return res_array
