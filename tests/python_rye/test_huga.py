from python_rye.hoge import Hoge


class TestHuga:
    def test_huga(self):
        assert Hoge().piyo() == "piyo"

    def test_error_case(self):
        raise AssertionError()
