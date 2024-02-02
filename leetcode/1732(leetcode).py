class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        for i in range(len(gain)):
            result.append(result[i] + gain[i])
        return max(result)
