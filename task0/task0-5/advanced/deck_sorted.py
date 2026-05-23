# 用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果
# 分别按照从大到小的顺序输出到 player1.txt，player2.txt，player3.txt，others.txt 四个文件中
import random


def creat_deck():
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = number * 4 + ["大王", "小王"]
    return deck


def shuffle_deal(deck):
    random.shuffle(deck)

    player1 = deck[0:17]
    player2 = deck[17:34]
    player3 = deck[34:51]
    remaining = deck[51:54]

    return player1, player2, player3, remaining


def sort(deck):
    order = {
        "3": 15,
        "4": 14,
        "5": 13,
        "6": 12,
        "7": 11,
        "8": 10,
        "9": 9,
        "10": 8,
        "J": 7,
        "Q": 6,
        "K": 5,
        "A": 4,
        "2": 3,
        "小王": 2,
        "大王": 1,
    }
    return sorted(deck, key=lambda card: order.get(card, 0))


def save(player1, player2, player3, remaining):
    player_1 = sort(player1)
    player_2 = sort(player2)
    player_3 = sort(player3)
    remaining_ = sort(remaining)

    with open("player1.txt", "w", encoding="utf-8") as f:
        f.write("玩家1的牌:\n" + " ".join(player_1))
    with open("player2.txt", "w", encoding="utf-8") as f:
        f.write("玩家2的牌:\n" + " ".join(player_2))
    with open("player3.txt", "w", encoding="utf-8") as f:
        f.write("玩家3的牌:\n" + " ".join(player_3))
    with open("others.txt", "w", encoding="utf-8") as f:
        f.write("底牌:\n" + " ".join(remaining_))


def main():
    deck = creat_deck()
    player1, player2, player3, remaining = shuffle_deal(deck)
    save(player1, player2, player3, remaining)


if __name__ == "__main__":
    main()
