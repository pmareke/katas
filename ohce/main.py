import sys
from ohce.src.ohce_runner import Ohce
from ohce.src.console_output import ConsoleOutput
from ohce.src.console_input import ConsoleInput
from ohce.src.custom_clock import CustomClock


def main() -> None:
    console_input = ConsoleInput()
    console_output = ConsoleOutput()
    custom_clock = CustomClock()
    ohce = Ohce(console_input, console_output, custom_clock)

    ohce.run(sys.argv[1])


if __name__ == "__main__":
    main()
