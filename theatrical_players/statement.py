from typing import Dict, List

from theatrical_players.play import PlayBuilder
from theatrical_players.amount import Amount
from theatrical_players.credit import Credit
from theatrical_players.report import Report


class Statement:

    def __init__(self) -> None:
        self.total_amount = Amount()
        self.volume_credits = Credit()
        self.lines: List[str] = []

    def process(self, invoice: Dict, plays: Dict) -> str:
        lines = self._generate_lines(invoice["performances"], plays)

        report = Report(invoice["customer"], lines)
        return report.generate(self.total_amount, self.volume_credits)

    def _generate_lines(self, performances: Dict, plays: Dict) -> List[str]:
        lines: List[str] = []
        for performace in performances:
            audience = performace["audience"]
            play = plays[performace['playID']]

            new_credit = Credit(max(audience - 30, 0))
            self.volume_credits.add(new_credit)

            play_build = PlayBuilder.build(play)
            amount, volume_credits = play_build.calculate(audience)
            self.total_amount.add(amount)
            self.volume_credits.add(volume_credits)

            line = f' {play["name"]}: {amount.format} ({audience} seats)'
            lines.append(line)
        return lines
