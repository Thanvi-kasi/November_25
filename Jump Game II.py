class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # if we've reached the end of the range for this jump
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
