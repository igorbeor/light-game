from random import randint


class Character():

    def __init__(self, name):
        self.name = name
        self.health_point = 100

    def deal_medium_damage_range(self, enemy):
        damage = randint(18, 25)
        enemy.health_point -= damage
        return damage

    def deal_high_damage_range(self, enemy):
        damage = randint(10, 35)
        enemy.health_point -= damage
        return damage

    def heal_yourself(self):
        heal = 0
        if self.health_point < 100:
            heal = randint(18, 25)
            health = self.health_point + heal
            self.health_point = health if health <= 100 else 100
        return heal