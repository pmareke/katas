# Introduction

For the purposes of practising TDD, this is one of the more advanced katas you can do. By now you should be proficient with the basic skills of TDD - the 3 Laws of TDD, the Rule of Three for duplication, and you should be experienced in how to structure a unit test (Arrange, Act, Assert).

This exercise allows you to refine the decision-making process for how you add tests. Done properly, you should be able to evolve the algorithm taking very small steps.

Doing it this way is a safe way to code: if you take a step that turns out as an unwise decision it is easier to reverse the step in your version control software and start anew. The ‘cost’ of doing this is minimal and it is generally easier to reverse and rethink than spending time debugging the code to find out what went wrong. Developers who are proficient in TDD generally spend a lot less time debugging code than simply opting out of their recent changes and trying another strategy.

The fast feedback you get from a small change means you can react immediately, rather than dealing with a problem that was introduced at some point previously where subsequent changes prior to the problem being detected can make it difficult to isolate. With small progressions, if you break something should very easy to isolate where you went wrong.

What’s recommended is that you support your decisions to progress using a heuristic such as the Transformation Priority Premise (see the "Articles" section below). This is an approach developed by Robert C. Martin (Uncle Bob) to help make TDD easier.

Transformations are best defined when compared to Refactorings. Refactorings are changes to the code that DO NOT change the code’s behaviour. Transformations are changes to the code that DO change the code’s behaviour, but in the context of TDD they are changes that allow the (current) failing test to pass, i.e. the code that is written to move the code from Red to Green.

In physics, the Second Law of Thermodynamics defines an arrow of progression where entropy moves from less to more. In TDD, there is an arrow of direction where the tests progress from being more specific to more generic. By defining the rules of Transformation Priority Premise, Uncle Bob has defined a series of ordered transformations. The transformations at the top of the list are the simplest. They become progressively more complex as you move down the list. By referencing and applying these transformation types, you can slowly and incrementally move your test suite from being specific to more generic.

This is a great exercise for practising test-driven algorithm design because you can start to familiarise yourself with using transformations to drive forward, but at the same time the direction of travel is not completely obscure. The rules for Roman Numerals (see below) would suggest a basic strategy, but you can try to use TPP to help pick the next step.

It’s relatively easy to know the next step is, but the point of the exercise is to try to let the TPP confirm your steps moving forward. It's advised to do this kata first choosing your own steps unaided, and then repeating it using the TPP to guide you.

## Instructions

Write a program to convert Arabic numbers into their Roman numeral equivalents.

The Romans wrote their numbers using combinations of the following letters:

```
Number	Numeral
1	I
5	V
10	X
50	L
100	C
500	D
1000	M
```

Initially, the Roman Numerals system consisted of expressing the number in terms of the most appropriate symbol that could be used.

To start, for the numbers 1-4, we would use the 'I' symbol in multiples to represent the number:

```
Number	Numeral
1	I
2	II
3	III
4	IIII
```

When the numbers got to 5, we would use 'V' as this symbol was the most efficient way to represent the number.

```
Number	Numeral
5	V
```

For the single integers greater than 5, a new rule came into effect: when 'smaller' symbols are appended one or more times behind the 'larger' symbol, it is considered to be added to the value representing the larger symbol.

```
Number	Numeral
6	VI
7	VII
8	VIII
9	VIIII
```

So, the initial sequence of Roman Numerals for the integers 1 - 9 were as follows:

```
1	2	3	4	5	6	7	8	9
I	II	III	IIII	V	VI	VII	VIII	VIIII
```

However, as you may have noticed the numbers for 4 and 9 don't look right. But the original formation of the numerals was this (even some clock faces still display IIII for 4). But this created problems as people kept confusing III with IIII and VIII with VIIII an additional rule was developed.

For numbers such as 4 and 9, the smaller symbol (I) is prepended with the larger symbol (V or 5 for the number 4, and X representing 10 for the number 9). When the smaller symbol appears before the larger symbol, it is considered to be subtracted from the larger symbol.

So, 'IV' is evaluated as: V - I = 5 - 1 = 4 and 'IX' is evaluated as: X - I = 10 - 1 = 9

Hence, the list of Roman Numerals for 1 - 9 are as amended to:

```
1	2	3	4	5	6	7	8	9
I	II	III	IV	V	VI	VII	VIII	IX
```

Because Roman system is follow a decimal notation system, the same rules apply for the next order up: units of 10. In this case, use the symbols, 'X' for 10, 'L' for fifty and 'C' for a hundred.

```
10	20	30	40	50	60	70	80	90
X	XX	XXX	XL	L	LX	LXX	LXXX	XC
```

For the next decimal order up, use the same rules again with 'C' for 100, 'D' for 500 and 'M' for 1000

```
100	200	300	400	500	600	700	800	900
C	CC	CCC	CD	D	DC	DCC	DCCC	CM
```

(As there are no symbols higher than 'M' (1000) the pattern stops here, and usually Roman Numerals don't consider numbers more than a few thousand)

There were certain rules that the numerals followed which should be observed:

 - The 'base 1' symbols ('I', 'X', 'C', 'M') can be subtracted from the next
   highest 'base 5' symbol ('V', 'L', 'D') or 'base 1' symbol, but only one
   occurrence is allowed. The symbol cannot be prepended to a symbol that is the
   next decimal order higher. So 'IV', 'IX' is ok but 'IL' or 'IC' are not.
   'XL', 'XC' is valid but XD and XM are not ('CD' and 'CM' are also valid).
 - The symbols 'I' and 'X' can be repeated at most 3 times in a row when the symbol is being appended
 - The 'base 5' symbols 'V', 'L' and 'D' can never be repeated.

More examples:

```
Number	Numeral
4	IV
9	IX
29	XXIX
80	LXXX
294	CCXCIV
2019	MMXIX
```
