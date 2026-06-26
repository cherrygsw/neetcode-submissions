class Solution:
    def twoSum(self, nums: List[int], target: int):
        previousMap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in previousMap:
                return [previousMap[diff], index]
            previousMap[num] = index
        return