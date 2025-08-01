

class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        self.hp -= self.atk()


chel = Hero("Chel", 40, 20)
boss = Hero("Boss", 100, 10)

# chel.attack()

