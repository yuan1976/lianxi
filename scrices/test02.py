import pytest


class Test02:
    """"""

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test03(self):
        print("03")


