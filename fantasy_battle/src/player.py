from fantasy_battle.src.damage import Damage
from fantasy_battle.src.equipment import Equipment
from fantasy_battle.src.inventory import Inventory
from fantasy_battle.src.item import Item
from fantasy_battle.src.stats import Stats
from fantasy_battle.src.target import SimpleEnemy, Target


class Player(Target):

    def __init__(self, inventory: Inventory, stats: Stats) -> None:
        self.stats = stats
        self.inventory = inventory

    def calculate_damage(self, other: Target) -> Damage:
        base_damage = self.__get_base_damage()
        damage_modifier = self.__get_damage_modifier()
        total_damage = round(base_damage * damage_modifier)
        soak = self.__get_soak(other, total_damage)
        return Damage(max(0, total_damage - soak))

    def __get_base_damage(self) -> float:
        inventory: Inventory = self.inventory
        equipment: Equipment = inventory.equipment
        left_hand: Item = equipment.left_hand
        right_hand: Item = equipment.right_hand
        head: Item = equipment.head
        feat: Item = equipment.feet
        chest: Item = equipment.chest
        return float(
            left_hand.base_damage +
            right_hand.base_damage +
            head.base_damage +
            feat.base_damage +
            chest.base_damage
        )

    def __get_damage_modifier(self) -> float:
        equipment: Equipment = self.inventory.equipment
        left_hand: Item = equipment.left_hand
        right_hand: Item = equipment.right_hand
        head: Item = equipment.head
        feet: Item = equipment.feet
        chest: Item = equipment.chest
        stats: Stats = self.stats
        strength_modifier: float = stats.strength * 0.1
        return float(
            strength_modifier +
            left_hand.damage_modifier +
            right_hand.damage_modifier +
            head.damage_modifier +
            feet.damage_modifier +
            chest.damage_modifier
        )

    @staticmethod
    def __get_soak(other: Target, total_damage: int) -> int:
        soak: int = 0
        if isinstance(other, Player):
            # TODO: Not implemented yet
            soak = total_damage
        elif isinstance(other, SimpleEnemy):
            simple_enemy: SimpleEnemy = other
            soak = round(
                simple_enemy.armor.damage_soak *
                (sum(
                    buff.soak_modifier
                    for buff in simple_enemy.buffs
                ) + 1)
            )
        return soak
