from typing import Dict, List, Optional


class SumPairs:
    @staticmethod
    def process(input: List[int], target: int) -> Optional[List[int]]:
        pairs: Dict[int, List[int]] = {}
        for x in range(0, len(input)):
            for y in range(x + 1, len(input)):
                x1 = input[x]
                y1 = input[y]
                if x1 + y1 == target:
                    pairs[y] = [x1, y1]

        if not pairs:
            return None

        smallest_index = sorted(pairs.keys())[0]
        return pairs[smallest_index]
