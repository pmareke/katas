from doublex import Mimic, Stub
from expects import expect, equal
from guess_random_number.guess import GuessRandomNumber
from guess_random_number.generator import RandomNumberGenerator


class TestGuessRandomNumber:
    def test_wins_in_the_first_guess(self) -> None:
        any_number = 0
        with Mimic(Stub, RandomNumberGenerator) as generator:
            generator.generate().returns(any_number)
        guess_random_number = GuessRandomNumber(generator)

        result = guess_random_number.guess_number(any_number)

        expect(result).to(equal(f"You win!!! {any_number} was the random number."))

    def test_not_wins_in_the_first_guess(self) -> None:
        any_number = 0
        with Mimic(Stub, RandomNumberGenerator) as generator:
            generator.generate().returns(any_number)
        guess_random_number = GuessRandomNumber(generator)

        error_message = "Sorry, {number} is not the number. Please try again."
        result = guess_random_number.guess_number(1)
        expect(result).to(equal(error_message.format(number=1)))

        result = guess_random_number.guess_number(2)
        expect(result).to(equal(error_message.format(number=2)))

        result = guess_random_number.guess_number(any_number)
        expect(result).to(equal(f"You win!!! {any_number} was the random number."))

    def test_loses_the_guess(self) -> None:
        any_number = 0
        with Mimic(Stub, RandomNumberGenerator) as generator:
            generator.generate().returns(any_number)
        guess_random_number = GuessRandomNumber(generator)

        error_message = "Sorry, {number} is not the number. Please try again."
        result = guess_random_number.guess_number(1)
        expect(result).to(equal(error_message.format(number=1)))

        result = guess_random_number.guess_number(2)
        expect(result).to(equal(error_message.format(number=2)))

        result = guess_random_number.guess_number(3)
        expect(result).to(
            equal(
                f"Sorry, you lose the game after 3 attemps. The number was {any_number}"
            )
        )

    def test_only_plays_three_times(self) -> None:
        any_number = 0
        with Mimic(Stub, RandomNumberGenerator) as generator:
            generator.generate().returns(any_number)
        guess_random_number = GuessRandomNumber(generator)

        guess_random_number.guess_number(1)
        guess_random_number.guess_number(1)
        guess_random_number.guess_number(1)
        result = guess_random_number.guess_number(1)

        error_message = (
            "Sorry, you lose the game after 3 attemps. The number was {number}"
        )
        expect(result).to(equal(error_message.format(number=any_number)))
