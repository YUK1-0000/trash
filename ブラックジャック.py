import random


cards_number = [["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"] for _ in range(4)]
player = []
show_cards = ""


for _ in range(2):
    player.append(cards_number[random.randint(0, 3)][random.randint(0,12)])


show_cards = (" ".join(player))
print(show_cards)