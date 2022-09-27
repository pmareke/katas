from typing import Dict, List, Optional


class SumPairs:

    @staticmethod
    def process(input_list: List[int], target: int) -> Optional[List[int]]:
        pairs: Dict[int, List[int]] = {}
        for first_index, _ in enumerate(input_list):
            for second_index in range(first_index + 1, len(input_list)):
                first_number = input_list[first_index]
                second_number = input_list[second_index]
                if first_number + second_number == target:
                    pairs[second_index] = [first_number, second_number]

        if not pairs:
            return None

        smallest_index = sorted(pairs.keys())[0]
        return pairs[smallest_index]
