class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            if i % 2 == 1:
                arr[i] = arr[i // 2] + 1
            else:
                arr[i] = arr[i // 2]
        return arr
