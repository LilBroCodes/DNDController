import pygame


class Item:
    def __init__(self, name: str, description: str, usable: bool, damage: MinMax):
        self.name = name


class MinMax:
    def __init__(self, minimum, maximum)
        self.min = minimum
        self.max = maximum

class Ability:
    def __init__(self, uses: int, name: str, damage: MinMax):
        self.uses = uses
        self.name = name
        self.damage = damage


class PlayerClass:
    def __init__(self, abilities: list[Ability], name: str, hp: int, inventory: dict[str]):
        self.abilities = abilities
        self.name = name
        self.hp = hp
        self.inventory = inventory
