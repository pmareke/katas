from typing import List

from fantasy_battle.src.armor import Armor
from fantasy_battle.src.buff import Buff


class Target:
    pass


class SimpleEnemy(Target):
    armor: Armor
    buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self.armor = armor
        self.buffs = buffs
