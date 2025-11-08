class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in pos:
                return [pos[y], i]
            pos[x] = i
        return []

