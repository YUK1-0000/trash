import random

class Game:
    cards = [["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] for _ in range(4)]
    player = []
    show_cards = ""

    def pass_(self):
        while True:
            sort = random.randint(0,3)
            num = random.randint(0,12)

            if self.cards[sort][num] != "":
                break
        
        self.player.append(self.cards[sort][num])
        self.cards[sort][num] = ""

    def show(self):
        self.show_cards = (" ".join(self.player))
    

game = Game
game.pass_()
game.show()