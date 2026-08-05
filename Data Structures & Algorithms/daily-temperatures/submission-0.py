class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # walk backwards
        # if stack empty = 0, add to stack
        # while day before > day, pop stack, add to stack
        # while day before < day, add to stack and set i to stack top
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)-1,-1,-1):
            if len(stack) == 0:
                res[i] = 0
                stack.append([temperatures[i], i])
            while temperatures[i] >= stack[-1][0]:
                stack.pop()
                if len(stack) == 0:
                    res[i] = 0
                    stack.append([temperatures[i], i])
                    break
            res[i] = stack[-1][1] - i
            stack.append([temperatures[i], i])
        return res
