class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        answer = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char == "(":
                stack.append(char)
            elif char == ")":
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 1
                else:
                    answer += 1
                if stack:
                    stack.pop()
                else:
                    answer += 1
            i += 1
        return answer + 2 * len(stack)
