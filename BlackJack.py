import random

class Game:
    cards_num = [["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] for _ in range(4)]
    cards_sort = ["♥", "♠", "♦", "☘"]
    score_10 = ["10", "J", "Q", "K"]
    player_nums = []
    player_sorts = []
    player_score = 0
    dealer_nums = []
    dealer_sorts = []
    dealer_score = 0
    A_in = False


    def pic_card(self):
        while True:
            sort = random.randint(0,3)
            num = random.randint(0,12)
            if self.cards_num[sort][num] != "":
                return sort, num


    def pass_player(self):
        sort, num = self.pic_card()
        self.player_nums.append(self.cards_num[sort][num])
        self.player_sorts.append(self.cards_sort[sort])
        self.cards_num[sort][num] = ""


    def pass_dealer(self):
        sort, num = self.pic_card()
        self.dealer_nums.append(self.cards_num[sort][num])
        self.dealer_sorts.append(self.cards_sort[sort])
        self.cards_num[sort][num] = ""


    def player_score_count(self):
        for i in range(len(self.player_nums)):
            if self.player_nums[i] == "A":
                self.player_score += 1
                self.A_in = True
            elif self.player_nums[i] in self.score_10:
                self.player_score += 10
            else:
                self.player_score += int(self.player_nums[i])


    def dealer_score_count(self):
        for i in range(len(self.dealer_nums)):
            if self.dealer_nums[i] == "A":
                self.dealer_score += 1
                self.A_in = True
            elif self.dealer_nums[i] in self.score_10:
                self.dealer_score += 10
            else:
                self.dealer_score += int(self.dealer_nums[i])


    def ready(self):
        for _ in range(2):
            self.pass_player()
            self.pass_dealer()
        

    def input_(self):
        while True:
            input_ = input("\nHit or Stand\n").upper()
            if input_ in ["HIT"]:
                print()
                return True
            elif input_ in ["STAND"]:
                print()
                return False


class UI(Game):

    def show_player_turn(self):
        print("Dealer", end = " ")
        self.dealer_hole()
        print("Player", end = " ")
        self.player_show()


    def show_dealer_turn(self):
        print("Player", end = " ")
        self.player_show()
        print("Dealer", end = " ")
        self.dealer_show()


    def player_show(self):
        for i in range(len(self.player_nums)):
            print(self.player_sorts[i], self.player_nums[i], end = " ")
        print()
    

    def dealer_show(self):
        for i in range(len(self.dealer_nums)):
            print(self.dealer_sorts[i], self.dealer_nums[i], end = " ")
        print()


    def dealer_hole(self):
        print(self.dealer_sorts[0], self.dealer_nums[1], end = " ")
        for i in range(len(self.dealer_nums)-1):
            print("?", end = " ")
        print()


game = UI()
game.ready()

print("\n~~ Player's turn ~~\n")
game.show_player_turn()
bust = False
while True:
    if game.input_():
        game.pass_player()
        game.show_player_turn()
        game.player_score_count()
        if game.player_score > 20:
            bust = True
            print("\nBust!")
            input("Enter to next")
            break
    else:
        break
print("\n~~ Dealer's turn ~~\n")
game.show_dealer_turn()
while True:
    if game.input_():
        game.pass_dealer()
        game.show_dealer_turn()
        game.dealer_score_count()
        if game.dealer_score > 20:
            print("Bust!")
            break
    else:
        break

if bust or game.dealer_score > game.player_score:
    print("Dealer Win")
elif game.player_score == game.dealer_score:
    print("Even")
else:
    print("Player Win")