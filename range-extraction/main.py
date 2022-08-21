from typing import List


class RangeExtraction:
    @staticmethod
    def extract(input: List[int]) -> str:
        return ",".join([str(x) for x in input])
