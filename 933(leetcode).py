from collections import deque


class RecentCounter:
    def __init__(self):
        self.answer = deque([])

    def ping(self, t: int) -> int:
        self.answer.append(t)
        while self.answer and self.answer[0] < t - 3000:
            self.answer.popleft()
        return len(self.answer)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
