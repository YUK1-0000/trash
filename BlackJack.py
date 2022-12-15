import random

class Game:

    CARDS_NUM = [["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] for _ in range(4)]
    CARDS_SORT = ["♥", "♠", "♦", "☘"]
    SCORE_10 = ["10", "J", "Q", "K"]
    player = 2
    player_nums = [[] for _ in range(player)]
    player_sorts = [[] for _ in range(player)]
    dealer_nums = []
    dealer_sorts = []


    def pic_card(self):
        while True:
            sort = random.randint(0,3)
            num = random.randint(0,12)
            if self.CARDS_NUM[sort][num] != "":
                return sort, num


    def pass_player(self, n):
        sort, num = self.pic_card()
        self.player_nums[n].append(self.CARDS_NUM[sort][num])
        self.player_sorts[n].append(self.CARDS_SORT[sort])
        self.CARDS_NUM[sort][num] = ""


    def pass_dealer(self):
        sort, num = self.pic_card()
        self.dealer_nums.append(self.CARDS_NUM[sort][num])
        self.dealer_sorts.append(self.CARDS_SORT[sort])
        self.CARDS_NUM[sort][num] = ""


    def player_score_count(self, n):
        player_score = 0
        A_in_player = 0
        for i in range(len(self.player_nums[n])):
            if self.player_nums[n][i] == "A":
                player_score += 1
                A_in_player += 1
            elif self.player_nums[n][i] in self.SCORE_10:
                player_score += 10
            else:
                player_score += int(self.player_nums[n][i])
        for i in range(A_in_player):
            if player_score <= 11:
                player_score += 10
        return player_score


    def dealer_score_count(self):
        dealer_score = 0
        A_in_dealer = 0
        for i in range(len(self.dealer_nums)):
            if self.dealer_nums[i] == "A":
                dealer_score += 1
                A_in_dealer += 1
            elif self.dealer_nums[i] in self.SCORE_10:
                dealer_score += 10
            else:
                dealer_score += int(self.dealer_nums[i])
        for i in range(A_in_dealer):
            if dealer_score <= 11:
                dealer_score += 10
        return dealer_score


    def ready(self):
        for _ in range(2):
            for i in range(self.player):
                self.pass_player(i)
            self.pass_dealer()
        

    def input_(self):
        while True:
            input_ = input(f"\nPlayer number + Hit or Stand\n").upper()
            if input_ == "HIT":
                print()
                return True
            elif input_ == "STAND":
                print()
                return False


class UI(Game):

    def player_turn_show(self, n):
        for i in range(len(self.player_nums[n])):
            print(self.player_sorts[n][i], self.player_nums[n][i], end = " ")
        print()
    

    def dealer_turn_show(self):
        for i in range(len(self.dealer_nums)):
            print(self.dealer_sorts[i], self.dealer_nums[i], end = " ")
        print()


    def dealer_hole(self):
        print(self.dealer_sorts[0], self.dealer_nums[0], end = " ")
        for _ in range(len(self.dealer_nums)-1):
            print("?", end = " ")
        print()

    def player_turn_ui(self):
        print("Dealer", end = "  ")
        self.dealer_hole()
        for i in range(self.player):
            print(f"Player{i+1}", end = " ")
            self.player_turn_show(i)


    def dealer_turn_ui(self):
        for i in range(self.player):
            print(f"Player{i+1}", end = " ")
            self.player_turn_show(i)
        print("Dealer", end = "  ")
        self.dealer_turn_show()


game = UI()
game.ready()

print("\n~~ Player's turn ~~\n")
player_bust = False
dealer_bust = False

game.player_turn_ui()
