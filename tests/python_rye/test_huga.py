from python_rye.huga import Huga


class TestHuga:
    def test_huga(self):
        assert Huga().piyo() == "piyo"
