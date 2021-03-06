# -*- coding: utf-8 -*-
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[-1]