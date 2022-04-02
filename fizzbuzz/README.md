# Introduction

This kata, taken from a popular children's maths game (or student drinking game), is the starting point on the TDD track. It's designed to be a semi-guided first stop for learning TDD from scratch.

We'll emphasise the following:

 - Start by writing a failing test for the simplest behaviour.
 - Implement the simplest amount of code needed to make the test pass.
 - As you add more tests, refactor to make the code more generic and more suitable.

## Instructions

Write a function that takes positive integers and outputs their string representation.

Your function should comply with the following additional rules:

 - If the number is a multiple of three, return the string "Fizz".
 - If the number is a multiple of five, return the string "Buzz".
 - If the number is a multiple of both three and five, return the string "FizzBuzz".

For example, given the numbers from 1 to 15 in order, the function would return:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```
