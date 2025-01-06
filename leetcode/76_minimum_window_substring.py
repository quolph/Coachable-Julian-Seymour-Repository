from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        deficits, surplus, t_counter = defaultdict(int), defaultdict(int), defaultdict(int)
        deficit_count = 0
        for char in t:
            deficits[char] += 1
            deficit_count += 1
            t_counter[char] += 1
        answer = ""
        left = right = 0
        while left <= right < len(s) + 1:
            # if there are no deficits, we have found a match
            if deficit_count == 0:
                # if we have not previously found an answer,
                # or the current window substring is shorter than our answer,
                # update the answer to the current window substring
                if not answer or right - left < len(answer):
                    answer = s[left:right]
                # move the left index up
                left_char = s[left]
                # if the character at the left index is in string t,
                if left_char in t_counter:
                    # and there is surplus of this left character in s,
                    if left_char in surplus and surplus[left_char] > 0:
                        # decrement the surplus
                        surplus[left_char] -= 1
                    else: # otherwise, there is now a deficit of the left character
                        deficits[left_char] += 1
                        deficit_count += 1
                left += 1
                # if necessary, move the right index forward so it isn't invalid
                if left > right:
                    right = left + 1
            elif right >= len(s): # if the right index has fallen off the valid range, break the loop
                break
            else: # there isn't a match, but the right index is still in valid range, so move it right
                right_char = s[right]
                # if the right character is in string t,
                if right_char in t_counter:
                    # and there was a noted deficit of that right character in s,
                    if right_char in deficits and deficits[right_char] > 0:
                        # decrement the deficit of right character
                        deficits[right_char] -= 1
                        deficit_count -= 1
                    else: #otherwise, there is a surplus. Increment it here
                        surplus[right_char] += 1
                right += 1
        return answer
