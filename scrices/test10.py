import pytest


class TestFixture:
    """"""

    def test01(self):
        print("")
        print("01")

    @pytest.mark.parametrize("name", ["张三"])
    def test02(self,name):
        print("")
        print(name)
