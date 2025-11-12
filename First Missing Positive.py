class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Replace all non-positive numbers and numbers > n with a dummy value (n+1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Mark existing numbers by flipping their corresponding index negative
        for num in nums:
            num = abs(num)
            if 1 <= num <= n:
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
        
        # Step 3: Find the first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # Step 4: If all indices are marked, return n + 1
        return n + 1
