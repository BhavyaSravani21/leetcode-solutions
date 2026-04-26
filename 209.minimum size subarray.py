class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=0
        min_len=float('inf')
        curr_sum=0
        for r in range(n):
            curr_sum+=nums[r]
            while curr_sum>=target:
                min_len=min(min_len,r-left+1)
                curr_sum-=nums[left]
                left+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
