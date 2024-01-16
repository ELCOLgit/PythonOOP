class Hero(object):
    """Basic template for hero. Contains name, power level and health
    points attributes. Implements the punch methods and string method."""

    def __init__(self, name="", power_level=1, health_points=100):
        self.__name = name
        self.health_points = health_points
        self.power_level = power_level

    def punch(self) -> float:
        """Return the punch power, which is 2 times the heroes level"""
        return self.power_level * 2

    def __str__(self):
        hero_info = f"Name: {self.__name}\n"
        hero_info += f"Power level: {self.power_level}\n"
        hero_info += f"Health points: {self.health_points}\n"

        return hero_info


class Support(Hero):
    def __init__(self, name="", power_level=1, health_points=100, healing=10):
        super().__init__(name, power_level, health_points)
        self.healing = healing
        
    def heal(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.health_points += amount
        else:
            print("Amount not valid")

    def attack(self) -> float:
        return self.power_level * 2
    
    def combat(self, other):
        if not isinstance(other, Monster):
            print("The hero only fights monsters.")
            return
        
        print(f"{self._Hero__name} engages in combat with {other.name}.")
        
        while True:
            other.health_points -= self.attack()
            
            if other.health_points <= 0:
                print(f"{other.name} is dead! {self._Hero__name} wins!")
                return True

            self.health_points -= other.attack()
            
            if self.health_points <= 0:
                print(f"{self._Hero__name} is dead! {other.name} wins.")
                return False


class Monster(object):
    def __init__(self, name="", strength=1, health_points=10, roar=""):
        self.name = name
        self.strength = strength
        self.health_points = health_points
        self.roar = roar
        print(self.roar)

    def attack(self) -> float:
        return self.strength * 1.5

    def __add__(self, other):
        if isinstance(other, Monster):
            return Monster(
                self.name + other.name,
                self.strength * other.strength,
                self.health_points + other.health_points,
                self.roar + other.roar + "!!!",
            )
        else:
            raise ValueError("There are not enough monsters.")


hero = Support(name="Bob", power_level=2, health_points=100, healing=10)

monster1 = Monster(name="Kyle", strength=7, health_points=150)
monster2 = Monster(name="Mike", strength=7, health_points=150)

monster3 = monster1 + monster2

for monster in [monster1, monster2, monster3]:
    if hero.health_points <= 0:
        print("The hero is dead, he cannot fight anymore.")
        break

    win = hero.combat(monster)

if win:
    print(f"{hero.name} won!")
else:
    print("The hero lost!")
