import logging
from decimal import Decimal
import pytest, unittest

from dlg_example_funcs import simple
from dlg_example_funcs import pi_bbp

logger = logging.Logger(__name__)

given = pytest.mark.parametrize


class TestMyFuncs(unittest.TestCase):
    def test_output(self):
        result = simple.output("World", kw="")
        self.assertEqual(result, "Hello World and ")

    def test_pi_k(self):
        result = pi_bbp.pi_k(0, 20)
        self.assertAlmostEqual(result, Decimal("3.141592653589793238462643381"))

    def test_pi_k_start_digit_wrong(self):
        with self.assertRaises(ValueError):
            _ = pi_bbp.pi_k(-1, 5)

    def test_pi_n_digits_wrong(self):
        with self.assertRaises(
            ValueError, msg="Invalid value of start_digit or n_digits provided!"
        ):
            _ = pi_bbp.pi_k(0, 0)
