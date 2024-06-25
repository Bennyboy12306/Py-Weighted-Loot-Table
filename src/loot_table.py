import random

class LootTable:
    def __init__(
        self, loot : dict
    ):
        self.loot = loot
             
    def sum_loot(self):
        total = 0
        for weight in self.loot.values():
            total += weight
        return total

    def pick_loot(self):
        stored_random = random.uniform(0, self.sum_loot())
        for key, weight in self.loot.items():
            if stored_random < weight:
                return key
            else:
                stored_random -= weight