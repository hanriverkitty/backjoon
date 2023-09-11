class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            if (
                "a" == s[i]
                or "e" == s[i]
                or "i" == s[i]
                or "o" == s[i]
                or "u" == s[i]
                or "A" == s[i]
                or "E" == s[i]
                or "I" == s[i]
                or "O" == s[i]
                or "U" == s[i]
            ):
                arr.append(i)

        result = list(s)
        print(arr)
        print(result)
        for i in range(0, len(arr) // 2):
            result[(arr[i])], result[(arr[len(arr) - 1])] = (
                result[(arr[len(arr) - 1])],
                result[(arr[i])],
            )
        ans = "".join(result)
        return ans


a = Solution()
a.reverseVowels("leetcode")
