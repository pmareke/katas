from typing import List


class Permutations:
    @staticmethod
    def process(input: str) -> List[str]:
        if len(input) == 1:
            return [input]

        permutations: List[str] = [input]

        for x in range(0, len(input)):
            for y in range(0, len(input)):
                if input[x] != input[y]:
                    tmp = [*input]
                    tmp[x] = input[y]
                    tmp[y] = input[x]
                    permutations.append("".join(tmp))

        return list(set(permutations))
