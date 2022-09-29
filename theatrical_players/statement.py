from typing import Dict, List

from theatrical_players.play import PlayBuilder
from theatrical_players.amount import Amount
from theatrical_players.report import Report


class Statement:

    def __init__(self) -> None:
        self.total_amount = Amount(0)
        self.volume_credits = 0
        self.lines: List[str] = []

    def process(self, invoice: Dict, plays: Dict) -> str:
        lines = self._generate_lines(invoice["performances"], plays)
        report = Report(invoice["customer"], lines)
        return report.generate(self.total_amount, self.volume_credits)

    def _generate_lines(self, performances: Dict, plays: Dict) -> List[str]:
        lines: List[str] = []
        for performace in performances:
            play = plays[performace['playID']]
            audience = performace["audience"]
            lines.append(self._generate_line(audience, play))
        return lines

    def _generate_line(self, audience: int, play: Dict) -> str:
        self.volume_credits += max(audience - 30, 0)

        play_build = PlayBuilder.build(play)
        amount, volume_credits = play_build.calculate(audience)
        self.total_amount += amount
        self.volume_credits += volume_credits

        return f' {play_build.name}: {amount.format} ({audience} seats)'
