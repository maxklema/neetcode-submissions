class Solution:
    def isValid(self, s: str) -> bool:
        tags = {"}": "{", "]": "[", ")": "("}
        stack = []
        for tag in s:
            if tag not in tags.keys():
                stack.append(tag)
            elif len(stack) > 0 and stack[len(stack) - 1] == tags[tag]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True
