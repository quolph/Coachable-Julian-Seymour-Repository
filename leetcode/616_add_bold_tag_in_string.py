class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        intervals = []
        for word in words:
            start = 0
            found = s.find(word, start)
            while found != -1 and start < len(s):
                interval = (found, found + len(word))
                intervals.append(interval)
                start = found + 1
                found = s.find(word, start)
        intervals.sort(key = lambda x: x[0])
        merged = []
        i = 0
        while i < len(intervals):
            interval1 = intervals[i]
            if i == len(intervals) - 1:
                merged.append(interval1)
                break
            else:
                start1, end1 = interval1
                for j in range(i + 1, len(intervals)):
                    start2, end2 = intervals[j]
                    if start2 <= end1:
                        end1 = max(end1, end2)
                        i = j + 1
                        if i == len(intervals):
                            merged.append((start1, end1))
                    else:
                        merged.append((start1, end1))
                        i = j
                        break
        if not merged:
            return s
        answer = []
        start, end = merged[0]
        if start > 0:
            answer.append(s[:start])
        prev = None
        for start, end in merged:
            if prev is not None:
                answer.append(s[prev:start])
            prev = end
            answer.append('<b>')
            answer.append(s[start:end])
            answer.append('</b>')
        if end < len(s):
            answer.append(s[end:])
        return ''.join(answer)
