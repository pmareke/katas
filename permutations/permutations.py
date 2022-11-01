class Permutations:

    def process(self, word: str) -> list[str]:
        if len(word) == 0:
            return []
        if len(word) == 1:
            return [word]

        permutations: list[str] = []
        for index, letter in enumerate(word):
            first = letter
            tail = word[:index] + word[index + 1:]

            for permutation in self.process(tail):
                item = first + permutation
                permutations.append("".join(item))

        return list(set(permutations))
