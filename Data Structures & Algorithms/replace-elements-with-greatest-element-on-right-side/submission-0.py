class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # reverse iteration
        # starting maxValue is -1
        # new maxValue = max(rightMax, arr[i])

        rightMax = -1
        for num in range(len(arr) - 1, -1, -1):
            maxValue = max(rightMax, arr[num])
            arr[num] = rightMax
            rightMax = maxValue
        
        return arr
        