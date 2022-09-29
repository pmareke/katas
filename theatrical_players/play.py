import math
from typing import Dict
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from theatrical_players.amount import Amount
from theatrical_players.credit import Credit


class PlayTypes(Enum):
    TRAGEDY = "tragedy"
    COMEDY = "comedy"


@dataclass  # type: ignore
class Play(ABC):
    name: str
    audience: int
    amount: Amount = Amount()
    credit: Credit = Credit()

    @abstractmethod
    def calculate(self) -> None:
        raise NotImplementedError()

    def __str__(self) -> str:
        return f' {self.name}: {self.amount.format} ({self.audience} seats)'


class TragedyPlay(Play):

    def calculate(self) -> None:
        self.credit = Credit()
        self.amount = Amount(
            int(40000 + 1000 *
                (self.audience - 30))) if self.audience > 30 else Amount()


class ComedyPlay(Play):

    def calculate(self) -> None:
        self.amount = Amount(30000 + (300 * self.audience))
        self.credit = Credit(math.floor(self.audience / 5))
        if self.audience > 20:
            self.amount.add(Amount(10000 + 500 * (self.audience - 20)))


class PlayBuilder:

    @staticmethod
    def build(play: Dict, audience: int) -> Play:
        play_type = play["type"]
        name = play["name"]
        try:
            return {
                PlayTypes.TRAGEDY: TragedyPlay(name, audience),
                PlayTypes.COMEDY: ComedyPlay(name, audience)
            }[PlayTypes(play_type)]
        except ValueError as exception:
            raise ValueError(f'unknown type: {play_type}') from exception
