import random


HAND_TYPES = ("グー","チョキ","パー")


while True:
    cpu_hand = random.randint(1,3)
    
    while True:
        my_hand = int(input("1:グー,2:チョキ,3:パー"))
        if my_hand in (1,2,3):
            break
    print("YOU:",HAND_TYPES[my_hand-1])
    print("CPU:",HAND_TYPES[cpu_hand-1])

    if HAND_TYPES[my_hand-1] == HAND_TYPES[cpu_hand-2]:
        print("勝ち！")
    elif HAND_TYPES[my_hand-2] == HAND_TYPES[cpu_hand-1]:
        print("負け！")
    else:
        print("あいこ！")
    while True:
        retry = int(input("1:もう一回 2:やめる"))
        if retry in (1, 2):
            break
    if retry-1:
        break