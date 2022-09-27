from typing import List


class Permutations:

    def process(self, word: str) -> List[str]:
        if len(word) == 0:
            return []
        if len(word) == 1:
            return [word]

        permutations: List[str] = []
        for index, letter in enumerate(word):
            first = letter
            tail = word[:index] + word[index + 1:]

            for permutation in self.process(tail):
                item = first + permutation
                permutations.append("".join(item))

        return list(set(permutations))
