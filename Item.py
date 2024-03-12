class item:
    items = []

    def __init__(self, gameobject, type, name, slot_type, stackable = False, maxStack = 1, isVisual = False):
        self.gameobject = gameobject
        self.name = name
        self.prefixes = {}
        if type == "material":
            self.slot_type = "material"
            self.stackable = stackable
            self.maxStack = maxStack
        elif type == "accessory":
            self.slot_type = "accessory"
            self.isVisual = isVisual
        elif type == "equipment":
            self.slot_type = slot_type
            self.isVisual = isVisual
        else:
            ValueError("Item type must be 'material', 'accessory' or 'equipment'.")
        item.items.append(self)

    def addPrefix(self, name, bonus):
        self.prefixes[name] = bonus

    def get_prefix(self, prefix_type: str):
        for prefix in self.prefixes:
            if prefix_type == prefix:
                return prefix
        FileNotFoundError("No attribute named: " + prefix_type + " found.")
        return None

    @staticmethod
    def getItem(name):
        return item.items[name]