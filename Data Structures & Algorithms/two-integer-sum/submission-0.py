class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            mn = target - n
            if mn in seen:
                return [seen[mn],i]
            else:
                seen[n] = i