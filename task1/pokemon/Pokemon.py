import random
from constant import TYPE_EFFECTIVENESS, TYPE_PASSIVES, POKEMON_DATA
from moves import *


class Pokemon:
    def __init__(self, name, data_dict):
        self.name = name
        self.hp = data_dict["hp"]
        self.max_hp = data_dict["hp"]
        self.base_attack = data_dict["attack"]
        self.attack = data_dict["attack"]
        self.defence = data_dict["defence"]
        self.element_type = data_dict["type"]
        self.dodge_rate = data_dict["dodge_rate"]
        self.moves = []
        self.status = None
        self.status_turns = 0
        self.passive_stack = 0
        self.shield = False
        self.digging = False
        self.parasitic_attacker = None
        self.fainted = False

    def __str__(self):
        status_str = f" | 状态: {self.status}" if self.status else ""
        return f"{self.name}({self.element_type}) HP: {self.hp}/{self.max_hp} 攻击: {self.attack} 防御: {self.defence}{status_str}"

    def take_damage(self, damage, move_type="一般"):
        # 土属性被动：免疫电属性伤害
        if self.element_type == "土" and move_type == "电":
            heal = int(self.max_hp * 0.2)
            self.hp = min(self.max_hp, self.hp + heal)
            print(f"{self.name} 的土属性吸收了电击，恢复了 {heal} 点HP！")
            return 0

        # 闪避判定
        if random.random() < self.dodge_rate:
            print(f"{self.name} 成功躲开了攻击！")
            if self.element_type == "电":
                print(f"{self.name} 的电引擎被激活，获得一次额外行动机会！")
                return "dodge_extra_turn"
            return "dodge"

        # 挖洞状态检查
        if self.digging == True:
            print(f"{self.name} 在地下，无法被击中！")
            self.digging = False
            return 0

        actual_damage = damage

        # 水属性被动
        if self.element_type == "水":
            if random.random() < 0.5:
                actual_damage = int(damage * 0.7)
                print(f"{self.name} 的水之护盾减免了部分伤害！")

        # 护盾检查
        if self.shield == True:
            actual_damage = int(damage * 0.5)
            self.shield = False
            print(f"{self.name} 的护盾发挥了作用！")

        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
            self.fainted = True
            print(f"{self.name} 昏厥了！")
        return actual_damage

    def apply_passive(self):
        passive = TYPE_PASSIVES.get(self.element_type, "")
        if "回复" in passive and "最大 HP" in passive:
            heal = int(self.max_hp * 0.1)
            self.hp = min(self.max_hp, self.hp + heal)
            print(f"{self.name} 的草之活力使它回复了 {heal} 点HP。")
        if self.status == "中毒" and not self.fainted:
            poison_damage = int(self.max_hp * 0.1)
            self.hp -= poison_damage
            print(f"{self.name} 受到中毒伤害，损失了 {poison_damage} 点HP。")
            self.status_turns -= 1
            if self.status_turns <= 0:
                self.status = None
                print(f"{self.name} 从中毒状态中恢复了。")
        elif self.status == "烧伤":
            self.hp -= 10
            print(f"{self.name} 受到烧伤伤害，损失了10点HP。")
            self.status_turns -= 1
            if self.status_turns <= 0:
                self.status = None
                print(f"{self.name} 从烧伤状态中恢复了。")
        elif self.status == "麻痹":
            if random.random() < 0.5:
                print(f"{self.name} 因麻痹而无法行动！")
                return False
            self.status_turns -= 1
            if self.status_turns <= 0:
                self.status = None
                print(f"{self.name} 从麻痹状态中恢复了。")
        if self.status == "寄生种子":
            drain = int(self.max_hp * 0.1)
            self.hp -= drain
            self.parasitic_attacker.hp = min(
                self.parasitic_attacker.max_hp, self.parasitic_attacker.hp + drain
            )
            print(
                f"寄生种子从 {self.name} 身上吸取了 {drain} 点HP，转移给了 {self.parasitic_attacker.name}。"
            )
            self.status_turns -= 1
            if self.status_turns <= 0:
                self.status = None
                print(f"{self.name} 身上的寄生种子消失了。")
        return True

    def use_move(self, move_index, target):
        if self.fainted:
            return None
        move = self.moves[move_index]
        if move.is_charge and move.charge_turns_remaining > 0:
            move.charge_turns_remaining -= 1
            if move.charge_turns_remaining == 0:
                damage = move.calculate_damage(self, target)
                effect_msg = move.apply_effect(self, target)
                return {
                    "move": move,
                    "damage": damage,
                    "effect": effect_msg,
                    "is_charging": False,
                }
            else:
                return {
                    "move": move,
                    "damage": 0,
                    "effect": f"{move.name} 还在蓄力...",
                    "is_charging": True,
                }
        # 正常技能
        if move.is_charge:
            move.charge_turns_remaining = move.charge_turns
            effect_msg = move.apply_effect(self, target)
            return {
                "move": move,
                "damage": 0,
                "effect": effect_msg,
                "is_charging": True,
            }
        damage = move.calculate_damage(self, target)
        effect_msg = move.apply_effect(self, target)
        if damage > 0 and self.element_type == "火" and self.passive_stack < 4:
            self.attack = int(self.base_attack * (1 + 0.1 * (self.passive_stack + 1)))
            self.passive_stack += 1
            print(f"{self.name} 的战斗怒火燃烧！攻击力提升至 {self.attack}。")
        return {
            "move": move,
            "damage": damage,
            "effect": effect_msg,
            "is_charging": False,
        }


# 属性子类
class GrassPokemon(Pokemon):
    def __init__(self, name, data_dict):
        super().__init__(name, data_dict)


class FirePokemon(Pokemon):
    def __init__(self, name, data_dict):
        super().__init__(name, data_dict)


class WaterPokemon(Pokemon):
    def __init__(self, name, data_dict):
        super().__init__(name, data_dict)


class ElectricPokemon(Pokemon):
    def __init__(self, name, data_dict):
        super().__init__(name, data_dict)


class GroundPokemon(Pokemon):
    def __init__(self, name, data_dict):
        super().__init__(name, data_dict)


# 具体宝可梦类
class PikaChu(ElectricPokemon):
    def __init__(self):
        super().__init__("皮卡丘", POKEMON_DATA["PikaChu"])
        self.moves = [Thunderbolt(), QuickAttack()]


class Bulbasaur(GrassPokemon):
    def __init__(self):
        super().__init__("妙蛙种子", POKEMON_DATA["Bulbasaur"])
        self.moves = [SeedBomb(), ParasiticSeeds()]


class Squirtle(WaterPokemon):
    def __init__(self):
        super().__init__("杰尼龟", POKEMON_DATA["Squirtle"])
        self.moves = [AquaJet(), Shield()]


class Charmander(FirePokemon):
    def __init__(self):
        super().__init__("小火龙", POKEMON_DATA["Charmander"])
        self.moves = [Ember(), FlameCharge()]


class Diglett(GroundPokemon):
    def __init__(self):
        super().__init__("地鼠", POKEMON_DATA["Diglett"])
        self.moves = [Scratch(), Dig()]


def get_pokemon(name):
    pokemon_classes = {
        "皮卡丘": PikaChu,
        "妙蛙种子": Bulbasaur,
        "杰尼龟": Squirtle,
        "小火龙": Charmander,
        "地鼠": Diglett,
    }
    if name in pokemon_classes:
        return pokemon_classes[name]()
    else:
        raise ValueError(f"未知的宝可梦: {name}")
