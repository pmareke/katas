class LeapYear:
    @staticmethod
    def calculate(year: int) -> bool:
        return (year % 400 == 0 or year % 100 != 0) and year % 4 == 0
