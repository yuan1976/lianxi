import pytest


class Test02:
    """"""
    @pytest.mark.run(order=3)
    def test03(self):
        print("03")

    @pytest.mark.run(order=1)
    def test01(self):
        print("01")

    @pytest.mark.run(order=4)
    def test04(self):
        print("04")

    @pytest.mark.run(order=2)
    def test02(self):
        print("02")
