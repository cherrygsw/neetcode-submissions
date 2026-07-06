class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        current = 0
        for n in nums:
            if n == 1:
                current += 1
            else:
                current = 0
            if current > output:
                output = current
        return output