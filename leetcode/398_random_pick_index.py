class Solution:
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)
    def pick(self, target: int) -> int:
        return self.indices[target][randint(0, len(self.indices[target]) - 1)]
