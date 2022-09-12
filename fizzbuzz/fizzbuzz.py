class FizzBuzz:
    @staticmethod
    def calculates(num: int) -> str:
        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
        return f"{num}" if result == "" else result
