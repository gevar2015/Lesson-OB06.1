import random
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


class Game:
    def __init__(self, player_name):
        """Инициализирует игру с игроком и компьютером."""
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """Начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет."""
        print("Начало игры!")
        print(self.player)
        print(self.computer)

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            damage = self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name} и наносит {damage} урона.")
            print(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            damage = self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name} и наносит {damage} урона.")
            print(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
