from typing import Dict, List

from theatrical_players.play import PlayBuilder
from theatrical_players.amount import Amount
from theatrical_players.credit import Credit
from theatrical_players.report import Report


class Statement:

    def __init__(self) -> None:
        self.total_amount = Amount()
        self.volume_credits = Credit()

    def process(self, invoice: Dict, plays: Dict) -> str:
        lines: List[str] = []
        for performace in invoice["performances"]:
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

        report = Report(invoice["customer"], lines)
        return report.generate(self.total_amount, self.volume_credits)
