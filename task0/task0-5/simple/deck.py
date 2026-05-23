# 斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别输出到
# player1.txt，player2.txt，player3.txt，others.txt 四个文件中，可以不要求牌的花色
import random


def creat_deck():
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = number * 4 + ["大王", "小王"]

    random.shuffle(deck)

    player1 = deck[0:17]
    player2 = deck[17:34]
    player3 = deck[34:51]
    remaining = deck[51:54]

    with open("player1.txt", "w", encoding="utf-8") as f:
        f.write("玩家1的牌:\n" + " ".join(player1))
    with open("player2.txt", "w", encoding="utf-8") as f:
        f.write("玩家2的牌:\n" + " ".join(player2))
    with open("player3.txt", "w", encoding="utf-8") as f:
        f.write("玩家3的牌:\n" + " ".join(player3))
    with open("others.txt", "w", encoding="utf-8") as f:
        f.write("底牌:\n" + " ".join(remaining))


creat_deck()
