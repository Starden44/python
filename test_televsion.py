import pytest
from television import *


def test_television_power():
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        self.tv = None

    def test_power_toggle(self):
        self.assertEqual(self.tv._Television__status, False)
        self.tv.power()
        self.assertEqual(self.tv._Television__status, True)
        self.tv.power()
        self.assertEqual(self.tv._Television__status, False)

if __name__ == "__main__":
    pytest.main()