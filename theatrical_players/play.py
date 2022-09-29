import math
from typing import Tuple, Dict
from abc import ABC, abstractmethod
from dataclasses import dataclass
from theatrical_players.amount import Amount
from theatrical_players.credit import Credit


@dataclass  # type: ignore
class Play(ABC):
    name: str

    @abstractmethod
    def calculate(self, audience: int) -> Tuple[Amount, Credit]:
        raise NotImplementedError()


class TragedyPlay(Play):

    def calculate(self, audience: int) -> Tuple[Amount, Credit]:
        credit = Credit()
        if audience > 30:
            return Amount(int(40000 + 1000 * (audience - 30))), credit
        return Amount(0), credit


class ComedyPlay(Play):

    def calculate(self, audience: int) -> Tuple[Amount, Credit]:
        amount = Amount(30000 + (300 * audience))
        credit = Credit(math.floor(audience / 5))
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
