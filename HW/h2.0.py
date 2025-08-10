# Родительский|Super класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lv = lvl
        self.hp = hp

    def action(self):
        print("pass")

# Дочерний класс мага
class HeroMage(Hero):
    def __init__(self, name, hp, mp, spell_book, lvl=1):
        super().__init__(name, lvl, hp)
        self.mp = mp
        self.spell_book = spell_book

    def action(self):
        print('base action')

    def cast_spell(self):
        if self.mp == 0:
            print('Сорян маны нет')
        else:
            self.mp -= 100
            print('Огненный щар')

    def rest(self):
        self.mp += 50
        print("Отдыхаю")

    def show_spells(self):
        print(f"доступные заклинаня: {self.spell_book}")

# Дочерний класс воина
class HeroWarrior(Hero):
    def __init__(self, name, lvl, hp, rage=0):
        super().__init__(name, lvl, hp)
        self.rage = rage

    def action(self):
        print("Герой готов к атаке!")

    def attack(self):
        if self.rage >= 100:
            print("герой наносит мощную атаку")
            self.rage = 0
        else:
            print("герой наносит обычную атаку")
            self.rage += 25


obj1 = Hero("John Doe", 10, 100)

mage = HeroMage(name="Merlin", hp=80, mp=500, lvl=5, spell_book=["Fireball", "Teleport"])
warrior = HeroWarrior(name="Conan", lvl=8, hp=150)


# Вызовы методов:
obj1.action()

mage.action()       # Выведет: base action
mage.show_spells()  # Выведет: доступные заклинаня: ['Fireball', 'Teleport']
warrior.action()    # Выведет: Герой готов к атаке!
warrior.attack()    # Выведет: герой наносит обычную атаку (и добавит 25 к rage)