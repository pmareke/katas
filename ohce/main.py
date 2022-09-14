import sys
from ohce.src.ohce_runner import Ohce
from ohce.src.console_output import ConsoleOutput
from ohce.src.custom_clock import CustomClock


def main() -> None:
    console_output = ConsoleOutput()
    custom_clock = CustomClock()
    ohce = Ohce(console_output, custom_clock)

    ohce.run(sys.argv[1])


if __name__ == "__main__":
    main()
