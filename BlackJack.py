import random

class Game:
    cards = [["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] for _ in range(4)]
    score_10 = ["10", "J", "Q", "K"]
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    A_in = False


    def pic_card(self):
        while True:
            sort = random.randint(0,3)
            num = random.randint(0,12)
            if self.cards[sort][num] != "":
                return sort, num


    def pass_player(self):
        sort, num = self.pic_card()
        self.player_cards.append(self.cards[sort][num])
        self.cards[sort][num] = ""


    def pass_dealer(self):
        sort, num = self.pic_card()
        self.dealer_cards.append(self.cards[sort][num])
        self.cards[sort][num] = ""


    def player_score_count(self):
        for i in range(len(self.player_cards)):
            if self.player_cards[i] == "A":
                self.player_score += 1
                self.A_in = True
            elif self.player_cards[i] in self.score_10:
                self.player_score += 10
            else:
                self.player_score += int(self.player_cards[i])


    def dealer_score_count(self):
        for i in range(len(self.dealer_cards)):
            match self.dealer_cards[i]:
                case "A":
                    self.dealer_score += 1
                    self.A_in = True
                case self.score_10:
                    self.dealer_score += 10
                case _:
                    self.dealer_score += int(self.dealer_cards[i])


    def ready(self):
        for _ in range(2):
            self.pass_player()
            self.pass_dealer()
        

    def input_(self):
        while True:
            input_ = input("Hit or Stand\n").upper()
            if input_ in ["HIT"]:
                return True
            elif input_ in ["STAND"]:
                return False


class UI(Game):

    def show(self):
        player_cards = (" ".join(self.player_cards))
        dealer_cards = (" ".join(self.dealer_cards))
        print(dealer_cards)
        print(player_cards)



game = UI()
game.ready()
game.show()
while True:
    if game.input_():
        game.pass_player()
        game.show()
        game.player_score_count()
        if game.player_score > 20:
            print("Bust!")
            break
    else:
        break