Feature: FizzBuzz

  Scenario Outline: FizzBuzz calculations
    Given the number "<number>"
     When calculates the result
     Then the result should be "<result>"

    Examples: FizzBuzzs
    | number         | result        |
    | 2              | 2             |
    | 4              | 4             |
    | 8              | 8             |
    | 3              | Fizz          |
    | 6              | Fizz          |
    | 9              | Fizz          |
    | 5              | Buzz          |
    | 10             | Buzz          |
    | 20             | Buzz          |
    | 15             | FizzBuzz      |
    | 30             | FizzBuzz      |
    | 45             | FizzBuzz      |
