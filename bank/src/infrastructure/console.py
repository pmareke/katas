from bank.src.domain.output import Output


class Console(Output):
    def print_line(self, line: str) -> None:
        print(line)
