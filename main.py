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
    print("How many do you want to generate?")
    count = int(input())
    for i in range(count):
        print(f"{i+1}/{count}" + " Chosen Loot: " + f"{loot_table.pick_loot()}")