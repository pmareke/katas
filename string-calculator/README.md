# Introduction

This is the third stop on the Test-Driven Development learning track. By now, you should be reasonably familiar with the concepts of "red, green, refactor" and "baby steps". If not, check out the earlier katas on this track: FizzBuzz and Leap Year.

This kata gives further practice at designing software feature-by-feature - an important part of Agile development processes - using TDD. Each time you add a new feature, you'll need to adapt your algorithm by refactoring to allow it to support the new behaviour.

The rules of this kata get steadily more complex. It is recommended that you approach this by adding one rule at a time. Try not to look ahead: imagine that the rules had arrived in separate briefings spread over a six-month project!

## Instructions

### Step 1

Create a simple String calculator with a single method:

```python
class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int
```

The method can take 1 or 2 comma-separated numbers, and will return their sum.

The method returns 0 when passed the empty string.

Example:

```python
StringCalculator().add("") // 0
StringCalculator().add("4") // 4
StringCalculator().add("1,2") // 3
```

Start with the simplest test case of an empty string and move to 1 and two numbers.

### Step 2

Allow the Add method to handle an unknown amount of numbers.

Example:

```python
StringCalculator().add("1,2,3,4,5,6,7,8,9") // 45
```

### Step 3

Allow the Add method to recognise newlines as well as commas as separators. The two separator types can be used interchangeably.

NB: Focus on the happy path - since this is not production code, it's fine if the code crashes if it's given invalid input (e.g. "1,\n2").

Example:

```python
StringCalculator().add("1\n2,3") // 6
```

### Step 4

Optionally support custom separators. To change separator, the beginning of the string will contain a separate line that looks like this: “//<separator>\n<numbers>”

Example:

```python
StringCalculator().add("//;\n1;2") // 3
```

### Step 5

Calling Add with a negative number will throw an exception negatives not allowed, and the negative that was passed.

If there are multiple negatives, show all of them in the exception message.

Example:

```python
StringCalculator().add("1,-2,-3") // error: negatives not allowed: -2 -3
```

### Step 6

Numbers bigger than 1000 should be ignored.

Example:

```python
StringCalculator().add("1001, 2") // 2
```

### Step 7

Separators can be of any length if surrounded by square brackets.

Example:

```python
StringCalculator().add("//[***]\n1***2***3") // 6
```

### Step 8

Allow multiple single-character separators like this: “//[delim1][delim2]\n”

Example:

```python
StringCalculator().add("//[*][%]\n1*2%3") // 6
```

### Step 9

Handle multiple separators with any character length.

Example:

```python
StringCalculator().add("//[foo][bar]\n1foo2bar3") // 6
```
