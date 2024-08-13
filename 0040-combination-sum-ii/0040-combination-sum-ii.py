class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # If the current value is the same as the one before, skip it to avoid duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the number and move to the next
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res
