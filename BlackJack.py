import random

class Game:

    CARDS_NUM = [["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] for _ in range(4)]
    CARDS_SORT = ["♥", "♠", "♦", "☘"]
    SCORE_10 = ["10", "J", "Q", "K"]
    while True:
        player = input("How many players? (1~8)\n")
        if player in [str(i+1) for i in range(8)]:
            player = int(player)
            break
    player_num_list = [i for i in range(player)]
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
        score = 0
        A_in_player = 0
        for i in range(len(self.player_nums[n])):
            if self.player_nums[n][i] == "A":
                score += 1
                A_in_player += 1
            elif self.player_nums[n][i] in self.SCORE_10:
                score += 10
            else:
                score += int(self.player_nums[n][i])
        for i in range(A_in_player):
            if score <= 11:
                score += 10
        return score


    def dealer_score_count(self):
        score = 0
        A_in_dealer = 0
        for i in range(len(self.dealer_nums)):
            if self.dealer_nums[i] == "A":
                score += 1
                A_in_dealer += 1
            elif self.dealer_nums[i] in self.SCORE_10:
                score += 10
            else:
                score += int(self.dealer_nums[i])
        for i in range(A_in_dealer):
            if score <= 11:
                score += 10
        return score


    def ready(self):
        for _ in range(2):
            for i in range(self.player):
                self.pass_player(i)
            self.pass_dealer()
        

    def player_input(self, done):
        while True:
            game.player_turn_table()            
            input_ = input(f"Player number + Hit or Stand\n").upper()
            if input_ == "":
                input_ += " "
            if input_[0] in done:
                print("You are already stand\n")
                continue
            elif input_[0] in [str(i+1) for i in range(self.player)]:
                n = int(input_[0])-1
                if input_[len(input_)-3:len(input_)+1] == "HIT":
                    return True, n
                elif input_[len(input_)-5:len(input_)+1] == "STAND":
                    return False, n
        

    def dealer_input(self):
        while True:
            game.dealer_turn_table()            
            input_ = input(f"\nHit or Stand\n").upper()
            match input_:
                case "HIT":
                    self.pass_dealer
                    game.dealer_turn_table()
                case "STAND":
                    break



    def player_turn(self):
        continue_ = True
        done = []
        print("\n~~ Player's turn ~~")
        while continue_:
            for i in range(self.player):
                if self.player_num_list[i] not in done:
                    break
            hit, n = self.player_input(done)
            if hit:
                self.pass_player(n)
            else:
                done.append(str(n))
            continue_ = False
            for i in range(self.player):
                if str(i) not in done:
                    continue_ = True
                    break

    
    def dealer_turn(self):
        print("\n~~ Dealer's turn ~~\n")
        while True:
             self.dealer_input()
             break


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

    def player_turn_table(self):
        print("\nDealer", end = "  ")
        self.dealer_hole()
        for i in range(self.player):
            print(f"Player{i+1}", end = " ")
            self.player_turn_show(i)
        print()


    def dealer_turn_table(self):
        for i in range(self.player):
            print(f"Player{i+1}", end = " ")
            self.player_turn_show(i)
        print("Dealer", end = "  ")
        self.dealer_turn_show()


    def result(self):
        print()
        dealer_score = self.dealer_score_count()
        for i in range(self.player):
            player_score = self.player_score_count(i)
            print(f"Player{i+1}", end = " ")
            if player_score > 21:
                print("Lose")
            elif player_score == dealer_score:
                print("Even")
            elif dealer_score > 21:
                print("Win")
            elif player_score > dealer_score:
                print("Win")
            else:
                print("Lose")
game = UI()
game.ready()
game.player_turn()
game.dealer_turn()
game.result()