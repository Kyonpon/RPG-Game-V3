import random

class Enemy:

    def __init__(self, type, health, physical_atk, magical_atk, magical_resistance, magical_weakness, alive):
        self.type = type
        self.health = health
        self.physical_atk = physical_atk
        self.magical_atk = magical_atk
        self.magical_resistance = magical_resistance
        self.magical_weakness = magical_weakness
        self.alive = alive
        # this will append all of the object of the Enemy class into enemy_list

    # These functions will get the specific attribute of an object of the Enemy class
    def get_type(self):
        return self.type

    def get_health(self):
        return self.health

    def get_physical_atk(self):
        return self.physical_atk

    def get_magical_atk(self):
        return self.magical_atk

    def get_magical_resist(self):
        return self.magical_resistance

    def get_magical_weakness(self):
        return self.magical_weakness

    def get_is_alive(self):
        return self.alive

# Here where you add Normal Enemies
# Normal Enemies
goblin = Enemy('Goblin', 50, 30, 0, 'NONE', 'NONE', True)
worm = Enemy('Worm', 50, 0, 30, 'NONE', 'NONE', True)
fire_golem = Enemy('Fire Golem', 150, 40, 70, 'FIRE', 'WATER', True)
water_golem = Enemy('Water Golem', 150, 40, 70, 'WATER', 'Fire', True)
wither = Enemy('Wither', 150, 40, 70, 'NONE', 'WATER', True)
skeleton = Enemy('Skelton', 60, 50, 0, 'NONE', 'NONE', True)

# Boss
demon = Enemy('Demon', 250, 80, 90, 'NONE', 'NONE', True)
minotour = Enemy('Minotour', 250, 80, 90, 'NONE', 'Fire', True)

# enemy randomizer
normal_enemy_list = [goblin, worm, fire_golem, water_golem, wither, skeleton]
boss_enemy_list = [demon,minotour]

randomized_norm_enemy_list = [i for i in normal_enemy_list]
random.shuffle(randomized_norm_enemy_list)