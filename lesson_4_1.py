from random import randint, choice, uniform
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    HACK = 5
    ANGEL_OR_CROW = 6


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage, defence_type):
        GameEntity.__init__(self, name, health, damage)
        self.__defence_type = defence_type
        self.__init_health = health

    @property
    def defence_type(self):
        return self.__defence_type

    @defence_type.setter
    def defence_type(self, value):
        self.__defence_type = value

    @property
    def init_health(self):
        return self.__init_health

    @init_health.setter
    def init_health(self, value):
        self.__init_health = value

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence_type = hero.super_ability_type


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability_type, damage_taken=0):
        GameEntity.__init__(self, name, health, damage)
        self.__super_ability_type = super_ability_type
        self.__damage_taken = damage_taken

    @property
    def super_ability_type(self):
        return self.__super_ability_type

    @super_ability_type.setter
    def super_ability_type(self, value):
        self.__super_ability_type = value

    @property
    def damage_taken(self):
        return self.__damage_taken

    @damage_taken.setter
    def damage_taken(self, value):
        self.__damage_taken = value

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior applied critical damage: {self.damage * coeff}')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_power(self, boss, heroes):
        add_damage = round(self.damage_taken * uniform(0.3, 0.5))
        boss.health -= add_damage
        print(f'Berserk applied super power: {add_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, value):
        self.__heal_points = value

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self is not hero:
                hero.health += self.__heal_points


class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = randint(2, 5)
        for hero in heroes:
            if hero.health > 0 and boss.health > 0 and hero.damage > 0:
                hero.damage += boost_point


class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.HACK)

    @property
    def hack_points(self):
        return self.__hack_points

    @hack_points.setter
    def hack_points(self, value):
        self.__hack_points = value

    def apply_super_power(self, boss, heroes):
        if round_number % 2 != 0:
            hack_points = randint(10, 30)
            alive_heroes = []
            for hero in heroes:
                if hero.health > 0 and self is not hero:
                    alive_heroes.append(hero)
            if boss.health > 0:
                boss.health -= hack_points
                random_alive_hero = choice(alive_heroes)
                random_alive_hero.health += hack_points
                print('Hack!')


class Druid(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.ANGEL_OR_CROW)


    is_round_for_perform = randint(1, 5)
    angel_or_crow = randint(1, 2)  # 1 - angel, 2 - crow

    def apply_super_power(self, boss, heroes):
        if self.is_round_for_perform == round_number:
            if self.angel_or_crow == 1:
                for hero in heroes:
                    try:
                        hero.heal_points += 10
                    except:
                        pass
            else:
                if boss.health < boss.init_health * 0.5:
                    boss.damage *= 1.5
                    round(boss.damage)






round_number = 0


def boss_hits(boss, heroes):
    for hero in heroes:
        if hero.health > 0:
            hero.health -= boss.damage
            hero.damage_taken = boss.damage




def heroes_hit(boss, heroes):
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 \
                and boss.defence_type != hero.super_ability_type:
            boss.health -= hero.damage
            hero.apply_super_power(boss, heroes)






def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f'\nROUND {round_number} ________________')
    print("BOSS " + str(boss) + " Defence: " + str(boss.defence_type))
    for hero in heroes:
        print(hero)



def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Gorilla", 900, 50, None)

    warrior = Warrior("Hektor", 270, 10)
    magic = Magic("Albert", 260, 15)
    doc = Medic("Aibolit", 240, 5, 15)
    berserk = Berserk("John", 280, 20)
    assistant = Medic("Strange", 290, 10, 5)
    hacker = Hacker('Mark', 280, 0)
    druid = Druid('Golum', 300, 0)

    heroes = [warrior, magic, doc, berserk, assistant, hacker, druid]
    medics = [doc, assistant]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)



start_game()















