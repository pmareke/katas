import datetime
from doublex import Mimic, Spy, Stub
from doublex_expects import have_been_called_with
from expects import expect
from print_date.src.calendar import Calendar

from print_date.src.print_date import PrintDate
from print_date.src.printer import Printer


class TestPrintDate:

    def test_prints_date_with_doublex(self) -> None:
        date = datetime.date(2023, 7, 13)
        spy_printer = Mimic(Spy, Printer)
        with Mimic(Stub, Calendar) as stub_calendar:
            stub_calendar.today().returns(date)
        print_date = PrintDate(spy_printer, stub_calendar)

        print_date.print_current_date()

        expect(spy_printer.print_line).to(have_been_called_with(date))
