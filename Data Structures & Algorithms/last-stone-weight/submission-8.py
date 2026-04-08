class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            n1 = -heapq.heappop(maxHeap)
            n2 = -heapq.heappop(maxHeap)

            if n1 != n2:
                heapq.heappush(maxHeap, -(n1 - n2))

        return -maxHeap[0] if maxHeap else 0
                

        