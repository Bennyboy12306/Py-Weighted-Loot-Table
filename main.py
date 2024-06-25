import random
from src.loot_table import LootTable

loot = {
    "Sword": 1,
    "Potion": 2,
    "Shield" : 4,
    "Helmet" : 4,
    "Coin" : 10
}


if __name__ == "__main__":
    loot_table = LootTable(loot)
    print("Chosen Loot: " + f"{loot_table.pick_loot()}")