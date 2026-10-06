class Solution:
    def __init__(self, nums):
        self.positions = {}
        for i, num in enumerate(nums):
            if num not in self.positions:
                self.positions[num] = []
            self.positions[num].append(i)
    def pick(self, target):
        return random.choice(self.positions[target])