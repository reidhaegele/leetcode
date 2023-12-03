class Solution:
    #O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i]
        
        post[len(nums)-1]=nums[-1]
        for j in range(len(nums) - 2, 0, -1):
            post[j] = post[j+1] * nums[j]
        
        answer = [1] * len(nums)
        for l in range(len(nums)):
            answer[l] = pre[l] * post[l]

#Brute force O(n^2)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 answer[i] = answer[i] * nums[j]
#             for l in range(0, i):
#                 answer[i] = answer[i] * nums[l]
#         return answer