class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                path.append(nums[i])
                backtrack(i, remaining - nums[i], path)  # reuse same number
                path.pop()

        backtrack(0, target, [])
        return res