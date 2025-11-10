from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # If we hit the target, add the current combination
            if total == target:
                res.append(path[:])
                return
            # If total exceeds target, stop exploring
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Include candidates[i] and explore further
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                # Backtrack (remove last element)
                path.pop()

        backtrack(0, [], 0)
        return res
