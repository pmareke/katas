from mars_rover import MarsRover
import pytest


class TestMarsRober:
    @pytest.mark.parametrize(
        "coordinates,position",
        [
            ("MMRMMLM", "2:3:N"),
            ("MMMMMMMMMM", "0:0:N"),
        ],
    )
    def test_rover_should_move(self, coordinates, position):
        mars = MarsRover()
        assert mars.execute(coordinates) == position
