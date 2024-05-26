import os
import json
import shutil


class item:
    items = []

    def __init__(self, name, health_addition, mana_addition, armor_addition, spritePath):
        self.name = name

        self.health_addition = health_addition
        self.mana_addition = mana_addition
        self.armor_addition = armor_addition

        self.spritePath = spritePath

    @staticmethod
    def serializeItemData(item):
        folder_name = f"{item.name}_ITEM_DATA"
        os.makedirs(folder_name, exist_ok=True)

        character_json = json.dumps(item.__dict__, indent=4)

        json_file_path = os.path.join(folder_name, "item.json")
        with open(json_file_path, "w") as file:
            file.write(character_json)

        if item.spritePath:
            sprite_file_name = os.path.basename(item.spritePath)
            sprite_dest_path = os.path.join(folder_name, sprite_file_name)
            if os.path.exists(item.spritePath):
                shutil.copyfile(item.spritePath, sprite_dest_path)
            else:
                print(f"Sprite image '{item.spritePath}' not found.")

    @staticmethod
    def getItem(name):
        return item.items[name]