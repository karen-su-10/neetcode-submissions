class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = left + (right - left) //2
            if nums[left] < nums[right]:
            # whole ascending[0,1,2,3,4]
            # move the right pointer to mid-1, search/cut on the left side
                return nums[left]
            elif nums[left] <= nums[mid]: #and nums[right] < nums[mid ]--implicit 
            #left side ascend, right side descend [3,4,5,1,2]
            # move the left pointer to mid+1, search/cut on the right side
                left = mid +1
        # if nums[left] > nums[mid] and nums[mid] < nums[right]: #whole descend [5,4,3,2,1]-- impossible case
        #     # move the left to mid +1, search on the right side
        #         left = mid +1
            else: #left descend, right ascend [4,5,1,2,3], rotation point on the left side , include mid
                right = mid
        return nums[left]

        
        
       
        