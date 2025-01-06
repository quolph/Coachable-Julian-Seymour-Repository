from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        found_odd = False
        for char, freq in counter.items():
            if freq % 2 != 0:
                if found_odd:
                    return False
                found_odd = True
        return True
