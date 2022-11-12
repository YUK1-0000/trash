import random


HAND_TYPES = ("グー","チョキ","パー")
my_hand = ""
cpu_hand = ""


while my_hand == cpu_hand:
    if my_hand:
        print("あいこ！")
    cpu_hand = random.randint(1,3)
    my_hand = ""
    
    while my_hand not in (1,2,3):
        my_hand = int(input("1:グー,2:チョキ,3:パー"))
    print("YOU:",HAND_TYPES[my_hand-1])
    print("CPU:",HAND_TYPES[cpu_hand-1])

    if my_hand > 1:
        if my_hand < cpu_hand:
            print("勝ち！")
        elif my_hand > cpu_hand:
            print("負け！")
    elif cpu_hand == 2:
        print("勝ち！")
    elif cpu_hand == 3:
        print("負け！")