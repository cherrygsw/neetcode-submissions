from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Use defaultdict to avoid key errors

        for s in strs:
            count = [0] * 26  # One slot for each letter a–z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)  # Convert to tuple for dict key

        return list(res.values())
