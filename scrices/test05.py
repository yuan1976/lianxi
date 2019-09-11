import pytest


class TestFixture:
    """"""

    @pytest.fixture()
    def b(self):
        print("03")

    def test01(self):
        print("")
        print("01")

    def test02(self,b):
        print("")
        print("02")
