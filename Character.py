import Item

class character:
    def __init__(self, health, stamina, armor, gameobject):
        self.gameobject = gameobject

        self.health = health
        self.stamina = stamina
        self.armor = armor

        self.attributes = []

        self.materials = {}
        self.equipment = {}
        self.accessories = {}

        self.maxmaterials = 0
        self.maxaccessories = 0
        self.differentequipmentslots = {}

    def addattribute(self, attribute, maxamount):
        self.attributes[attribute] = maxamount

    def removeattribute(self, attribute):
        self.attributes.pop(attribute)

    def addmaterialslot(self):
        self.maxmaterials +=1

    def removemateriaslot(self):
        self.maxmaterials -=1

    def addaccessorylot(self):
        self.maxaccessories +=1

    def removeaccessorylot(self):
        self.maxaccessories -=1

    def addequipmentslot(self, slot_name):
        self.equipment[slot_name] = None

    def removeequipmentslot(self, slot_name):
        self.equipment.pop(slot_name)

    def boostattribute(self):
        combined = self.equipment | self.accessories
        if combined == {}:
            print("The character doesn't have any equipment or accessory items")
            return
        for item in combined.items():
            for prefix, boost in item.prefixes.items():
                if prefix in self.attributes:
                    self.attributes[prefix] += boost
                else:
                    self.addattribute(prefix, boost)