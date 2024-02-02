import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        a = []
        for _ in range(len(nums)):
            a.append(heapq.heappop(nums))
        a.reverse()
        return a[k - 1]
