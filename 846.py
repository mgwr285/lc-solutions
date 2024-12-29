class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        pq = list(counter.keys())
        heapq.heapify(pq)
        while pq:
            for i in range(pq[0], pq[0] + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != pq[0]:
                        return False
                    heapq.heappop(pq)
        return True
