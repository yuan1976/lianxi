import pytest


@pytest.fixture(autouse=True, scope="class")
def a():
    print("")
    print("a")

@pytest.mark.usefixtures()
class TestFixture:
    """"""

    def test01(self):
        print("")
        print("01")

    def test02(self):
        print("")
        print("02")
