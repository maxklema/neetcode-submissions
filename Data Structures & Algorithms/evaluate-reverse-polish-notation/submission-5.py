class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            match char:
                case "+":
                    stack.append((int(stack.pop()) + int(stack.pop())))
                case "-":
                    f = int(stack.pop())
                    s = int(stack.pop())
                    stack.append(s - f)
                case "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                case "/":
                    f = stack.pop()
                    s = stack.pop()
                    res = int(s) / int(f)
                    if (res < 0):
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                    stack.append(res)
                case _:
                    stack.append(char)

        return int(stack.pop())
