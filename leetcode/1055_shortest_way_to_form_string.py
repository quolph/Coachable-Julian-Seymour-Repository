class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_counter = defaultdict(int)
        target_counter = defaultdict(int)
        for char in source:
            source_counter[char] += 1
        for char in target:
            if char not in source_counter:
                return -1
            target_counter[char] += 1
        temp_source = []
        for char in source:
            if char in target_counter:
                temp_source.append(char)
        source = ''.join(temp_source)
        temp_source = None
        i = j = 0
        answer = 0
        while i < len(target) and j < len(source):
            if source[j] == target[i]:
                i += 1
            j += 1
            if j == len(source):
                answer += 1
                j = 0
            elif i == len(target):
                answer += 1
        return answer
