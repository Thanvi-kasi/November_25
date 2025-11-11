class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If current number is greater than remaining target, break early
                if candidates[i] > target:
                    break
                
                # Choose candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()  # Backtrack
        
        backtrack(0, target, [])
        return res
