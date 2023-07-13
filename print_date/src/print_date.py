from print_date.src.calendar import Calendar
from print_date.src.printer import Printer


class PrintDate:
    def __init__(self, printer: Printer, calendar: Calendar) -> None:
        self.printer = printer
        self.calendar = calendar

    def print_current_date(self) -> None:
        date = self.calendar.today()
        self.printer.print_line(date)
