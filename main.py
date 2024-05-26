class Hero:
    def __init__(self, name):
        """Инициализирует героя с именем, здоровьем и силой удара."""
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        """Атакует другого героя, отнимая здоровье в размере своей силы удара."""
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

    def is_alive(self):
        """Возвращает True, если здоровье героя больше 0, иначе False."""
        return self.health > 0

    def __str__(self):
        return f"{self.name}: здоровье={self.health}, сила удара={self.attack_power}"
