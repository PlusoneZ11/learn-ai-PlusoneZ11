import json


def save():
    # 定义数据的默认值
    game_data = {"character": None, "affinity": 0, "story": "1.1", "choice": {}}
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(game_data, f)


def load():
    # 读取存档文件
    with open("save.json", "r", encoding="utf-8") as f:
        game_data = json.load(f)
    # 显示存档信息
    print(f"角色:{game_data['character']}")
    print(f"好感度:{game_data['affinity']}")
    print(f"进度:{game_data['progress']}")
    return game_data
