# Sum of Pairs

- Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
- If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.
- Negative numbers and duplicate numbers can and will appear.

```python
sum_pairs([11, 3, 7, 5], 10)
# returns [3, 7]

sum_pairs([4, 3, 2, 3, 4], 6)
# returns [4, 2]

sum_pairs([0, 0, -2, 3], 2)
# returns None

sum_pairs([10, 5, 2, 3, 7, 5], 10)
# returns [3, 7]
```
