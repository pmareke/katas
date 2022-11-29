from fantasy_battle.src.equipment import Equipment


class Inventory:
    def __init__(self, equipment: Equipment) -> None:
        self.equipment = equipment
