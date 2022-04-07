from typing import Callable


class MarsRover:
    X = 0
    Y = 0
    direction = "N"

    def execute(self, instructions: str) -> str:
        commands = {
            "M": self._move,
            "L": self._rotate,
            "R": self._rotate,
        }
        for instruction in instructions:
            fn: Callable = commands[instruction]
            fn(instruction)

        return f"{self.X}:{self.Y}:{self.direction}"

    def _move(self, instruction: str) -> None:
        if self.direction == "N":
            self.Y = self._increase_position(self.Y)
        elif self.direction == "S":
            self.Y = self._decrease_position(self.Y)
        elif self.direction == "E":
            self.X = self._increase_position(self.X)
        else:
            self.X = self._decrease_position(self.X)

    def _increase_position(self, current_position: int) -> int:
        return (current_position + 1) % 10

    def _decrease_position(self, current_position: int) -> int:
        return (current_position - 1) % 10

    def _rotate(self, instruction: str) -> None:
        moves = {
            "N": "W" if instruction == "L" else "E",
            "S": "E" if instruction == "L" else "W",
            "E": "N" if instruction == "L" else "S",
            "W": "S" if instruction == "L" else "N",
        }
        self.direction = moves[self.direction]
