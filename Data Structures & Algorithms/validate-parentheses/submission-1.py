class Solution:
    def isValid(self, s: str) -> bool:
        tagsOpen = {"{": "}", "[": "]", "(": ")"}
        tagsClosed = {"}": "{", "]": "[", ")": "("}
        stack = []
        for tag in s:
            if tag in tagsOpen.keys():
                stack.append(tag)
            elif len(stack) > 0 and stack[len(stack) - 1] == tagsClosed[tag]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True
