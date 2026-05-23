# 队伍选择、回合制战斗、胜负判定
import random
from Pokemon import get_pokemon


class Game:
    def __init__(self):
        self.available_pokemons = ["皮卡丘", "妙蛙种子", "杰尼龟", "小火龙", "地鼠"]
        self.player_team = []
        self.computer_team = []
        self.player_active = None
        self.computer_active = None

    def select_teams(self):
        print("请选择 3 个宝可梦用于组成你的队伍：")
        for i, name in enumerate(self.available_pokemons, 1):
            pokemon = get_pokemon(name)
            print(f"{i}. {name}({pokemon.element_type}属性）", end=" ")
        print()
        while True:
            try:
                choices = input("输入数字选择你的宝可梦（用空格分隔）: ").split()
                indices = [int(c) - 1 for c in choices]
                if len(set(indices)) != 3 or any(
                    i < 0 or i >= len(self.available_pokemons) for i in indices
                ):
                    print("输入无效，请重新选择3个不同的宝可梦。")
                    continue
                self.player_team = [
                    get_pokemon(self.available_pokemons[i]) for i in indices
                ]
                break
            except:
                print("输入无效，请重新选择3个不同的宝可梦.")
        computer_choices = random.sample(range(len(self.available_pokemons)), 3)
        self.computer_team = [
            get_pokemon(self.available_pokemons[i]) for i in computer_choices
        ]
        print("你的队伍:", [p.name for p in self.player_team])
        print("电脑的队伍:", [p.name for p in self.computer_team])

    def choose_active(self):
        print("\n请选择你的出战宝可梦：")
        for i, pokemon in enumerate(self.player_team, 1):
            print(f"{i}.{pokemon.name}（{pokemon.element_type}属性）", end=" ")
        print()
        while True:
            try:
                choice = int(input("输入数字选择你的宝可梦: ")) - 1
                if (
                    0 <= choice < len(self.player_team)
                    and not self.player_team[choice].fainted
                ):
                    self.player_active = self.player_team[choice]
                    break
                else:
                    print("无效选择或该宝可梦已昏厥，请重新选择。")
            except:
                print("输入无效，请重新选择。")

        for pokemon in self.computer_team:
            if not pokemon.fainted:
                self.computer_active = pokemon
                break

        print(f"你选择了 {self.player_active.name}！")
        print(f"电脑选择了 {self.computer_active.name}！")

    def player_turn(self):
        print(f"\n你的 {self.player_active.name} 的技能：")
        for i, move in enumerate(self.player_active.moves, 1):
            print(f"{i}. {move.name}: {move.description}")
        while True:
            try:
                choice = (
                    int(input(f"选择一个技能 (1-{len(self.player_active.moves)}): "))
                    - 1
                )
                if 0 <= choice < len(self.player_active.moves):
                    result = self.player_active.use_move(choice, self.computer_active)
                    if result["is_charging"]:
                        print(f"{self.player_active.name} {result['effect']}")
                    else:
                        if result["damage"] > 0:
                            origin_dodge = self.computer_active.dodge_rate
                            self.computer_active.dodge_rate += result[
                                "move"
                            ].extra_dodge
                            damage_result = self.computer_active.take_damage(
                                result["damage"], result["move"].move_type
                            )
                            self.computer_active.dodge_rate = origin_dodge
                            if damage_result == "dodge_extra_turn":
                                print(
                                    f"{self.computer_active.name} 成功躲开并获得了额外行动机会！"
                                )
                            elif damage_result == "dodge":
                                print(f"{self.computer_active.name} 成功躲开了攻击！")
                            else:
                                print(
                                    f"{self.player_active.name} 使用了 {result['move'].name}！"
                                )
                                print(
                                    f"{self.computer_active.name} 受到了 {damage_result} 点伤害！剩余 HP：{self.computer_active.hp}"
                                )
                        if result["effect"]:
                            print(result["effect"])
                    break
                else:
                    print("无效选择。")
            except Exception as e:
                print(f"程序内部报错: {e}")

    def computer_turn(self):
        available_moves = [i for i, move in enumerate(self.computer_active.moves)]
        if not available_moves:
            return
        move_index = random.choice(available_moves)
        result = self.computer_active.use_move(move_index, self.player_active)
        if result["is_charging"]:
            print(f"{self.computer_active.name} {result['effect']}")
        else:
            if result["damage"] > 0:
                original_dodge = self.player_active.dodge_rate
                self.player_active.dodge_rate += result["move"].extra_dodge
                damage_result = self.player_active.take_damage(
                    result["damage"], result["move"].move_type
                )
                self.player_active.dodge_rate = original_dodge

                if damage_result == "dodge_extra_turn":
                    print(f"{self.player_active.name} 成功躲开并获得了额外行动机会！")
                    self.player_turn()
                elif damage_result == "dodge":
                    print(f"{self.player_active.name} 成功躲开了攻击！")
                else:
                    print(f"{self.computer_active.name} 使用了 {result['move'].name}！")
                    print(
                        f"{self.player_active.name} 受到了 {damage_result} 点伤害！剩余 HP：{self.player_active.hp}"
                    )
            if result["effect"]:
                print(result["effect"])

    def battle_loop(self):
        print("战斗开始！")
        round_num = 1
        while True:
            print(f"\n--- 第 {round_num} 回合 ---")
            print(f"你的 {self.player_active}")
            print(f"电脑的 {self.computer_active}")

            if not self.player_active.apply_passive():
                # 如果麻痹导致无法行动，则跳过玩家回合
                pass
            else:
                self.player_turn()
            if self.computer_active.fainted:
                if not self._check_fainted():
                    print("\n恭喜！你战胜了所有电脑的宝可梦！")
                    return "player"

            if not self.computer_active.apply_passive():
                pass
            else:
                self.computer_turn()
            if self.player_active.fainted:
                if not self._check_fainted():
                    print("\n很遗憾，你的所有宝可梦都昏厥了...")
                    return "computer"

            # 检查胜负
            if all(p.fainted for p in self.computer_team):
                print("\n恭喜！你战胜了所有电脑的宝可梦！")
                return "player"
            if all(p.fainted for p in self.player_team):
                print("\n很遗憾，你的所有宝可梦都昏厥了...")
                return "computer"

            round_num += 1

    def _check_fainted(self):
        if self.computer_active.fainted:
            print(f"{self.computer_active.name} 昏厥了！")
            for pokemon in self.computer_team:
                if not pokemon.fainted:
                    self.computer_active = pokemon
                    print(f"电脑派出了 {self.computer_active.name}！")
                    return True  # 成功替换，还有宝可梦可以战斗
            return False  # 电脑队伍全灭
        if self.player_active.fainted:
            print(f"{self.player_active.name} 昏厥了！")
            avaliable = [pokemon for pokemon in self.player_team if not pokemon.fainted]
            if not avaliable:
                return False
            print("请选择下一个出战的宝可梦：")
            for i, pokemon in enumerate(self.player_team, 1):
                status = "(已昏厥)" if pokemon.fainted else ""
                print(f"{i}. {pokemon.name}{status}", end=" ")
            print()
            while True:
                try:
                    choice = int(input("输入数字选择你的宝可梦: ")) - 1
                    if (
                        0 <= choice < len(self.player_team)
                        and not self.player_team[choice].fainted
                    ):
                        self.player_active = self.player_team[choice]
                        print(f"你派出了 {self.player_active.name}！")
                        return True
                    else:
                        print("无效选择或该宝可梦已昏厥，请重新选择。")
                except:
                    print("输入无效，请重新选择。")
        return True

    # 主入口
    def run(self):
        print("欢迎来到宝可梦对战游戏！")
        self.select_teams()
        self.choose_active()
        result = self.battle_loop()
        print(
            f"\n游戏结束！{'你获得了胜利！' if result == 'player' else '很遗憾，电脑获得了胜利。'}"
        )


if __name__ == "__main__":
    game = Game()
    game.run()
