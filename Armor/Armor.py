class Armor:
    def __init__(self, health):
        self.health = health

    def take_hit(self, damage):
        self.health -= damage
        return
