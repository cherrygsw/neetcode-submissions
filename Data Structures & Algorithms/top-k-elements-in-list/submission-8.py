class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        
        sortedPairs = sorted(hashMap.items(), key=lambda pair: pair[1], reverse = True)

        result = []
        for i in range(k):
            result.append(sortedPairs[i][0])
        return result

        