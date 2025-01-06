class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = cursor = 0
        star = -1
        while j < len(s):
            if i < len(p) and p[i] in ["?", s[j]]:  #match found, increment both cursors
                i += 1
                j += 1
            elif i < len(p) and p[i] == "*":        #if we encounter an *
                star, cursor = i, j                     # save the position of the *
                i += 1                                  # increment pattern cursor
            elif star != -1:                        # if we previously encountered an asterisk,
                i = star + 1                            # move i to the right of where the * was found
                cursor += 1                             # increment the saved string cursor position
                j = cursor                              # move the string cursor to the saved position + 1
            else:
                return False
        while i < len(p) and p[i] == "*":   # clean up for trailing *s
            i+= 1
        return i == len(p)
