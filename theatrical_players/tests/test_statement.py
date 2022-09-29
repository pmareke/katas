import json

import pytest
from approvaltests import verify
from approvaltests.utils import get_adjacent_file

from theatrical_players.statement import Statement

class TestStatement:
    def test_example_statement(self) -> None:
        with open(get_adjacent_file("invoice.json")) as f:
            invoice = json.loads(f.read())
        with open(get_adjacent_file("plays.json")) as f:
            plays = json.loads(f.read())

        statement = Statement(invoice, plays)
        verify(statement.process())


    def test_statement_with_new_play_types(self) -> None:
        with open(get_adjacent_file("invoice_new_plays.json")) as f:
            invoice = json.loads(f.read())
        with open(get_adjacent_file("new_plays.json")) as f:
            plays = json.loads(f.read())
        with pytest.raises(ValueError) as exception_info:
            statement = Statement(invoice, plays)
            statement.process()
        assert "unknown type" in str(exception_info.value)