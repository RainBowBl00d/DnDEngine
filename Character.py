import json
import os
class character:
    def __init__(self, name, maxhealth, maxmana, maxarmor, maxinventoryslots):
        self.name = name
        self.spritePath = ""

        self.currenthealth = maxhealth
        self.currentmana = maxmana
        self.currentarmor = maxarmor

        self.maxhealth = maxhealth
        self.maxmana = maxmana
        self.maxarmor = maxarmor

        self.maxinventoryslots = maxinventoryslots

    def addHealth(self, amount):
        if self.currenthealth + amount <= self.maxhealth:
            self.currenthealth += amount
        else:
            self.currenthealth = self.maxhealth

    def subtractHealth(self, amount):
        if self.currenthealth - amount < 0:
            pass
            #Do dying stuff
        else:
            self.currenthealth -= amount

    def addMana(self, amount):
        if self.currentmana + amount <= self.maxmana:
            self.currentmana += amount
        else:
            self.currentmana = self.maxmana

    def subtractMana(self, amount):
        if self.currentmana - amount < 0:
            self.currentmana = 0
        else:
            self.currentmana -= amount

    @staticmethod
    def serializeCharacterData(character):
        folder_name = f"{character.name}_DATA"
        os.makedirs(folder_name, exist_ok=True)

        character_json = json.dumps(character.__dict__, indent=4)

        json_file_path = os.path.join(folder_name, "character.json")
        with open(json_file_path, "w") as file:
            file.write(character_json)

        if character.spritePath:
            sprite_file_name = os.path.basename(character.spritePath)
            sprite_dest_path = os.path.join(folder_name, sprite_file_name)
            if os.path.exists(character.spritePath):
                os.replace(character.spritePath, sprite_dest_path)
            else:
                print(f"Sprite image '{character.spritePath}' not found.")

