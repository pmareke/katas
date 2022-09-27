from guess_random_number.generator import RandomNumberGenerator


class GuessRandomNumber:

    def __init__(self, generator: RandomNumberGenerator) -> None:
        self.random_number = generator.generate()
        self.attemps = 0

    def guess_number(self, guess_number: int) -> str:
        if guess_number == self.random_number:
            return f"You win!!! {self.random_number} was the random number."
        self.attemps += 1
        if self.attemps >= 3:
            return f"Sorry, you lose the game after 3 attemps. The number was {self.random_number}"
        return f"Sorry, {guess_number} is not the number. Please try again."
