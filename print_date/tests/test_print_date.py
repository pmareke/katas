import datetime
from typing import Any

from doublex import Mimic, Spy, Stub
from doublex_expects import have_been_called_with
from expects import be_true, expect

from print_date.src.calendar import Calendar
from print_date.src.print_date import PrintDate
from print_date.src.printer import Printer


class StubCalendar(Calendar):
    def __init__(self, date: datetime.date) -> None:
        self.date = date

    def today(self) -> datetime.date:
        return self.date


class SpyPrinter(Printer):
    def __init__(self) -> None:
        self.message = None

    def print_line(self, message: Any) -> None:  # type: ignore
        self.message = message

    def print_line_have_been_called_with(self, message: Any) -> bool:  # type: ignore
        return bool(self.message == message)


class TestPrintDate:

    def test_prints_date_with_doublex(self) -> None:
        spy_printer = Mimic(Spy, Printer)
        date = datetime.date(2023, 7, 13)
        with Mimic(Stub, Calendar) as stub_calendar:
            stub_calendar.today().returns(date)
        print_date = PrintDate(spy_printer, stub_calendar)

        print_date.print_current_date()

        expect(spy_printer.print_line).to(have_been_called_with(date))

    def test_prints_date_with_custom_doubles(self) -> None:
        spy_printer = SpyPrinter()
        date = datetime.date(2023, 7, 13)
        stub_calendar = StubCalendar(date)
        print_date = PrintDate(spy_printer, stub_calendar)

        print_date.print_current_date()

        expect(spy_printer.print_line_have_been_called_with(date)).to(be_true)
