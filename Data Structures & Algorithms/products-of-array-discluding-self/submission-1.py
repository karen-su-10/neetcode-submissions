class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use an array pre, pre[i] stores the product until i-1, this needs products, so assign [1]
        n= len(nums)
        pre = [1] * n
        post = [1] * n
        
        #step from left
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        #step from right, n-1 is the last item, n-2 is the second last item, exclusive -1 means stop at 0, go left -1 at a time
        for i in range(n - 2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
            
        #construct output[i] = pre[i]
        output = [0] * n
        for i in range(0, n):
            output[i] = pre[i] * post[i]
        return output