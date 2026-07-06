class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = set()
        for num in nums:
            if num in newArr:
                return True
            newArr.add(num)
        return False