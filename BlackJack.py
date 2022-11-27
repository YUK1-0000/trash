import random


cards_number = [[i+1 for i in range(13)] for _ in range(4)]
player = []

player.append(cards_number[random.randint(0, 3)])