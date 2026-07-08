class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)          # dedup + O(1) membership
        best = 0

        for x in s:
            # only start a run at sequence starts
            if x - 1 not in s:
                length = 1
                y = x + 1
                while y in s:
                    length += 1
                    y += 1
                best = max(best, length)

        return best
