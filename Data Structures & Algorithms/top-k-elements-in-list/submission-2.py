class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = {}

        for num in nums:
            numCounts[num] = numCounts.get(num,0) + 1

        sortedCounts = sorted(numCounts.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sortedCounts[:k]]