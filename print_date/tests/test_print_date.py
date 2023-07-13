from print_date.src.print_date import PrintDate


class TestPrintDate:

    def test_prints_date(self) -> None:
        print_date = PrintDate()

        print_date.print_current_date()

        # I don't know how to test it
