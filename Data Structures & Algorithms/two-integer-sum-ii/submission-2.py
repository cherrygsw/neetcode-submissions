class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1          # two pointers at ends

        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:                  # found the unique pair
                return [i + 1, j + 1]        # 1-indexed as required
            if s < target:                   # sum too small → move left pointer right
                i += 1
            else:                            # sum too large → move right pointer left
                j -= 1
