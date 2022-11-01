from collections.abc import Callable


class MarsRover:
    x_coordinate = 0
    y_coordinate = 0
    direction = "N"

    def execute(self, instructions: str) -> str:
        commands = {
            "M": self._move,
            "L": self._rotate,
            "R": self._rotate,
        }
        for instruction in instructions:
            callback: Callable = commands[instruction]
            callback(instruction)

        return f"{self.x_coordinate}:{self.y_coordinate}:{self.direction}"

    def _move(self, _instruction: str) -> None:
        if self.direction == "N":
            self.y_coordinate = self._increase_position(self.y_coordinate)
        elif self.direction == "S":
            self.y_coordinate = self._decrease_position(self.y_coordinate)
        elif self.direction == "E":
            self.x_coordinate = self._increase_position(self.x_coordinate)
        else:
            self.x_coordinate = self._decrease_position(self.x_coordinate)

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
