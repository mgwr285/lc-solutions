class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq, waiting = [], deque()
        for count in Counter(tasks).values():
            pq.append(-count)
        heapq.heapify(pq)
        t = 0
        while pq or waiting:
            t += 1
            if pq:
                count = heapq.heappop(pq)
                if count + 1 < 0:
                    waiting.append((t + n, count + 1))
            if waiting and waiting[0][0] == t:
                heapq.heappush(pq, waiting.popleft()[1])
        return t
