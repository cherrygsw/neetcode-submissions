class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # store numbers we've already seen
        for n in nums:  # loop through each number in nums
            if n in seen:  # if number already in set, it's a duplicate
                return True  # return True immediately when duplicate found
            seen.add(n)  # add number to set for future checks
        return False  # no duplicates found after full loop
