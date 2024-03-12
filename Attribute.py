class attribute():
    def __init__(self, name, minamount, maxamount, currentamount, item=None, character=None):
        if character == None:
            self.item = item
        elif item == None:
            self.character = character
        else:
            ValueError("Both item and character can't be None")
        self.name = name
        self.minamount = minamount
        self.maxamount = maxamount
        self.currentamount = currentamount

    def add(self, amount):
        if self.currentamount + amount < self.maxamount:
            self.currentamount += amount
        else:
            print("Tried to go over maximum allowed for " + self.name + ", item: " + self.item.name)
            self.currentamount = self.maxamount

    def subtract(self, amount):
        if self.currentamount - amount > self.minamount:
            self.currentamount -= amount
        else:
            print("Tried to go below mininum allowed for" + self.name + ", item: " + self.item.name)
            self.currentamount = self.minamount

    def setmaxamount(self, amount):
        self.maxamount = amount

    def setminamount(self, amount):
        self.minamount = amount