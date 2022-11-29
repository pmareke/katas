class Armor:
    damage_soak: int


class SimpleArmor(Armor):
    def __init__(self, damage_soak: int) -> None:
        self.damage_soak = damage_soak
