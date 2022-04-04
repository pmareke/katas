from mars_rover import MarsRover
class TestMarsRober:
    def test_rover_should_move(self):
        assert MarsRover().execute("MMRMMLM") == "2:3:N"
