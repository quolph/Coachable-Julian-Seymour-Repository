class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        memo = {2:2}
        def helper(n):
            if n not in memo:
                memo[n] = helper(n - 1) + 2 * (n - 1)
            return memo[n]
        counter = defaultdict(int)
        for age in ages:
            counter[age] += 1
        ages = sorted(counter.keys(), reverse=True)
        count = 0
        for x in range(len(ages)):
            if counter[ages[x]] > 1 and 0.5 * ages[x] + 7 < ages[x]:
                count += helper(counter[ages[x]])
            for y in range(x + 1, len(ages)):
                if 0.5 * ages[x] + 7 < ages[y] <= ages[x]:
                    count += counter[ages[x]] * counter[ages[y]]
        return count
