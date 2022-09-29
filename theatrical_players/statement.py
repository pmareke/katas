from typing import Dict, List

from theatrical_players.play import PlayBuilder, Play
from theatrical_players.report import Report


class Statement:

    def __init__(self, report: Report = Report()) -> None:
        self.report = report

    def process(self, invoice: Dict, plays: Dict) -> str:
        calculated_plays: List[Play] = []
        for performace in invoice["performances"]:
            audience = performace["audience"]
            play_id = plays[performace["playID"]]

            play_build = PlayBuilder.build(play_id, audience)
            play_build.calculate()

            calculated_plays.append(play_build)

        return self.report.generate(invoice["customer"], calculated_plays)
