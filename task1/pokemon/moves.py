import random
from constant import TYPE_EFFECTIVENESS


class Move:
    def __init__(
        self,
        name,
        power_mult,
        move_type,
        description,
        is_charge=False,
        charge_turns=0,
        extra_dodge=0.0,
    ):
        self.name = name
        self.power_mult = power_mult  # 威力倍数
        self.move_type = move_type  # 技能属性
        self.description = description  # 技能描述
        self.is_charge = is_charge  # 是否为蓄力技能
        self.charge_turns = charge_turns  # 蓄力回合数
        self.charge_turns_remaining = 0  # 剩余蓄力回合
        self.extra_dodge = extra_dodge  # 额外闪避率

    def calculate_damage(self, attacker, target):
        base_damage = int(attacker.attack * self.power_mult)
        # 属性克制计算
        if self.move_type in TYPE_EFFECTIVENESS:
            if TYPE_EFFECTIVENESS[self.move_type]["克制"] == target.element_type:
                base_damage *= 2
                print(f"效果拔群！")
            elif TYPE_EFFECTIVENESS[target.element_type]["克制"] == self.move_type:
                base_damage *= 0.5
                print(f"效果不理想...")
        # 防御力减免
        final_damage = max(1, base_damage - target.defence)
        return final_damage

    def apply_effect(self, attacker, target):
        return None


# 具体技能实现
class Thunderbolt(Move):
    def __init__(self):
        super().__init__(
            "十万伏特", 1.4, "电", "对敌人造成1.4倍电属性伤害，有10%概率使敌人麻痹"
        )

    def apply_effect(self, attacker, target):
        if random.random() < 0.1:
            target.status = "麻痹"
            target.status_turns = random.randint(1, 2)
            return f"{target.name} 麻痹了！下回合无法行动。"
        return None


class QuickAttack(Move):
    def __init__(self):
        super().__init__("电光一闪", 1.0, "一般", "快速攻击，有10%概率触发第二次攻击")

    def calculate_damage(self, attacker, target):
        damage = super().calculate_damage(attacker, target)
        if random.random() < 0.1:
            damage += super().calculate_damage(attacker, target)
            print("快速连击")
        return damage


class SeedBomb(Move):
    def __init__(self):
        super().__init__("种子炸弹", 1.2, "草", "造成草属性伤害，15%几率使目标中毒")

    def apply_effect(self, attacker, target):
        if random.random() < 0.15:
            target.status = "中毒"
            target.status_turns = 3
            return f"{target.name} 中毒了！"
        return None


class ParasiticSeeds(Move):
    def __init__(self):
        super().__init__(
            "寄生种子", 0.5, "草", "每回合吸取对手10%最大生命值，持续3回合"
        )

    def apply_effect(self, attacker, target):
        target.status = "寄生种子"
        target.status_turns = 3
        target.parasitic_attacker = attacker
        return f"寄生种子种在了 {target.name} 身上！"


class AquaJet(Move):
    def __init__(self):
        super().__init__("水枪", 1.4, "水", "喷射强力水流，造成1.4倍水属性伤害")


class Shield(Move):
    def __init__(self):
        super().__init__("护盾", 0.0, "水", "生成护盾，下回合减伤50%")

    def apply_effect(self, attacker, target):
        attacker.shield = True
        return f"{attacker.name} 使用了护盾！"


class Ember(Move):
    def __init__(self):
        super().__init__("火花", 1.0, "火", "造成火属性伤害，10%几率使目标烧伤")

    def apply_effect(self, attacker, target):
        if random.random() < 0.1:
            target.status = "烧伤"
            target.status_turns = 2
            return f"{target.name} 烧伤了！"
        return None


class FlameCharge(Move):
    def __init__(self):
        super().__init__(
            "蓄能爆炎",
            3.0,
            "火",
            "蓄力1回合后造成3倍伤害，80%几率烧伤敌人",
            is_charge=True,
            charge_turns=1,
            extra_dodge=0.2,
        )

    def apply_effect(self, attacker, target):
        if random.random() < 0.8:
            target.status = "烧伤"
            target.status_turns = 2
            return f"{target.name} 被严重烧伤了！"
        return None


class Scratch(Move):
    def __init__(self):
        super().__init__("抓", 1.0, "一般", "用爪子抓伤敌人，造成普通伤害")


class Dig(Move):
    def __init__(self):
        super().__init__(
            "挖洞",
            1.8,
            "地面",
            "潜入地下蓄力，下回合发动攻击",
            is_charge=True,
            charge_turns=1,
        )

    def apply_effect(self, attacker, target):
        attacker.digging = True
        return f"{attacker.name} 挖洞躲入了地下！"
