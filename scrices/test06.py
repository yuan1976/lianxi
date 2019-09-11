import pytest


@pytest.fixture(autouse=True)
def a():
    print("")
    print("a")


class TestFixture:
    """"""

    def test01(self):
        print("")
        print("01")

    def test02(self):
        print("")
        print("02")
