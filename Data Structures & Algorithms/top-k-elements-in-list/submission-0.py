class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        heap = []
        for x in freq:
            heapq.heappush(heap, (freq[x], x))
            if len(heap) > k:
                heapq.heappop(heap)
        return[x for freq, x in heap]
        