class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # have a hashmap that has paired values (value:key) with value:index

        for i, n in enumerate(nums): # returns both value(n) and index(i)
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i
        return