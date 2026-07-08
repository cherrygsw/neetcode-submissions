class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = []
        for num in nums:
            if num in newArr:
                return True
            newArr.append(num)
        return False