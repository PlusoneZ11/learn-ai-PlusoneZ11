# 定义游戏中的常量数据

TYPE_EFFECTIVENESS = {
    "草": {"克制": "水", "被克制": "火"},
    "火": {"克制": "草", "被克制": "水"},
    "水": {"克制": "火", "被克制": "电"},
    "电": {"克制": "水", "被克制": "草"},
    "土": {"克制": "电", "被克制": "水"},
}
TYPE_PASSIVES = {
    "草": "每回合回复 10% 最大 HP 值",
    "火": "每次造成伤害,叠加 10% 攻击力,最多 4 层",
    "水": "受到伤害时,有 50% 的几率减免 30% 的伤害",
    "电": "当成功躲闪时,可以立即使用一次技能",
    "土": "受到电属性攻击时，免疫该次伤害"
}
POKEMON_DATA = {
    "PikaChu": {
        "hp": 80, 
        "attack": 35, 
        "defence": 5, 
        "type": "电", 
        "dodge_rate": 0.3
    },
    "Bulbasaur": {
        "hp": 100,
        "attack": 35,
        "defence": 10,
        "type": "草",
        "dodge_rate": 0.1,
    },
    "Squirtle": {
        "hp": 80,
        "attack": 25,
        "defence": 20,
        "type": "水",
        "dodge_rate": 0.2,
    },
    "Charmander": {
        "hp": 80,
        "attack": 35,
        "defence": 15,
        "type": "火",
        "dodge_rate": 0.1,
    },
    "Diglett": {
        "hp": 100,
        "attack": 15,
        "defence": 30,
        "type": "土",
        "dodge_rate": 0.3,
    },
}
