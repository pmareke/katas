import math
from typing import Tuple, Dict
from abc import ABC, abstractmethod
from dataclasses import dataclass
from theatrical_players.amount import Amount


@dataclass  # type: ignore
class Play(ABC):
    name: str

    @abstractmethod
    def calculate(self, audience: int) -> Tuple[Amount, int]:
        raise NotImplementedError()


class TragedyPlay(Play):

    def calculate(self, audience: int) -> Tuple[Amount, int]:
        if audience > 30:
            return Amount(int(40000 + 1000 * (audience - 30))), 0
        return Amount(0), 0


class ComedyPlay(Play):

    def calculate(self, audience: int) -> Tuple[Amount, int]:
        amount = Amount(30000 + (300 * audience))
        credit = math.floor(audience / 5)
        if audience > 20:
            return amount + Amount(10000 + 500 * (audience - 20)), credit
        return amount, credit


class PlayBuilder:

    @staticmethod
    def build(play: Dict) -> Play:
        play_type = play["type"]
        name = play["name"]
        if play_type == "tragedy":
            return TragedyPlay(name)
        if play_type == "comedy":
            return ComedyPlay(name)
        raise ValueError(f'unknown type: {play_type}')
