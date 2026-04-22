class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack or pairs[stack.pop()]!=ch:
                    return False
        return not stack