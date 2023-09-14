class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0 for i in range(n + 1)]
        result[0] = 0
        if n >= 1:
            result[1] = 1
        if n >= 2:
            result[2] = 1
        for i in range(3, n + 1):
            result[i] = result[i - 3] + result[i - 2] + result[i - 1]
        return result[n]
