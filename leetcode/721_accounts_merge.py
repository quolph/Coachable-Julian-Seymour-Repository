class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            email_addresses = account[1:]
            for i in range(len(email_addresses)):
                src = email_addresses[i]
                if src not in graph:
                    graph[src] = set()
                for j in range(i + 1, len(email_addresses)):
                    dest = email_addresses[j]
                    graph[src].add(dest)
                    graph[dest].add(src)
        answer = []
        for account in accounts:
            name = account[0]
            email_address = account[1]
            if email_address not in graph:
                continue
            email_addresses = set()
            queue = deque([email_address])
            while queue:
                email_address = queue.popleft()
                if email_address not in graph:
                    continue
                email_addresses.add(email_address)
                neighbors = graph.pop(email_address)
                for neighbor in neighbors:
                    if neighbor not in graph:
                        continue
                    queue.append(neighbor)
            answer.append([name] + sorted(list(email_addresses)))
        answer.sort(key=lambda x: x[0])
        return answer
