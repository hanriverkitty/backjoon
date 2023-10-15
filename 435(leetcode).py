class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                pre_day = stack.pop()
                answer[pre_day] = cur_day - pre_day

            stack.append(cur_day)
        return answer
