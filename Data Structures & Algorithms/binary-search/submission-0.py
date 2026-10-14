class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            p = (left + right) // 2
            current = nums[p]
            if current == target:
                return p
            elif current < target:
                left = p + 1
            else:
                right = p - 1
        return -1
