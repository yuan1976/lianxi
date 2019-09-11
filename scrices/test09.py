import pytest


@pytest.fixture()
def a():
    print("")
    print("a")

@pytest.mark4()
class TestFixture:
    """"""

    def test01(self):
        print("")
        print("01")

    def test02(self):
        print("")
        print("02")
