class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
# given array nums, return the most times 1's appears consecutively in array
        outcome = 0
        current = 0
        for n in nums:
            if n == 1:
                current += 1
                outcome = max(current,outcome)
            else:
                current = 0
        return outcome
            

