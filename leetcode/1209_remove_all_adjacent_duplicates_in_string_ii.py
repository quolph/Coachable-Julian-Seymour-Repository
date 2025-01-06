class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack:
                prev_char, count = stack[-1]
                if char == prev_char:
                    count += 1
                    if count == k:
                        stack.pop()
                    else:
                        stack[-1] = (char, count)
                else:
                    stack.append((char, 1))
            else:
                stack.append((char, 1))
        answer = []
        for char, count in stack:
            for i in range(count):
                answer.append(char)
        return ''.join(answer)
