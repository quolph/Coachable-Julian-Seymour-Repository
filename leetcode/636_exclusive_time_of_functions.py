class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = [0] * n
        stack = []
        prev = 0
        for log in logs:
            splat = log.split(":")
            function_id = int(splat[0])
            interval_type = splat[1]
            timestamp = int(splat[2])
            if interval_type == "start":
                if stack:
                    answer[stack[-1]] += timestamp - prev
                stack.append(function_id)
                prev = timestamp
            else:
                answer[stack.pop()] += timestamp - prev + 1
                prev = timestamp + 1
        return answer
    def exclusiveTimeSlow(self, n: int, logs: List[str]) -> List[int]:
        answer = [0] * n
        stack = []
        starts = defaultdict(list)
        intervals = defaultdict(list)
        for log in logs:
            splat = log.split(":")
            function_id = int(splat[0])
            interval_type = splat[1]
            timestamp = int(splat[2])
            if interval_type == "start":
                if stack:
                    prev = stack[-1]
                    intervals[prev].append((starts[prev].pop(), timestamp))
                stack.append(function_id)
                starts[function_id].append(timestamp)
            else:
                stack.pop()
                intervals[function_id].append((starts[function_id].pop(), timestamp + 1))
                if stack:
                    prev = stack[-1]
                    starts[prev].append(timestamp + 1)
        merged = defaultdict(list)
        for function_id in intervals:
            prev_start = prev_end = -1
            sortedd = sorted(intervals[function_id])
            for i in range(len(sortedd)):
                interval = sortedd[i]
                start, end = interval
                if start > prev_end:
                    if -1 < prev_start < prev_end:
                        merged[function_id].append((prev_start, prev_end))
                    prev_start = start
                prev_end = end
                if i == len(sortedd) - 1:
                    merged[function_id].append((prev_start, end))
        intervals = None
        for function_id in merged:
            for interval in merged[function_id]:
                start, end = interval
                time = end - start
                answer[function_id] += time
        return answer
