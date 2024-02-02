class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        a = max(candies)
        print(a)
        for i in candies:
            if i + extraCandies >= a:
                result.append("true")
            else:
                result.append("false")
        print(result)
        return result


c = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
c.kidsWithCandies(candies, extraCandies)
