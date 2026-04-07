import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    def test_median_odd(self):
        engine = StatEngine([1, 3, 2])
        self.assertEqual(engine.get_median(), 2)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_error_handling(self):
        with self.assertRaises(ZeroDivisionError):
            StatEngine([])

    def test_std_dev_known_outcome(self):
        # Population std dev of [2, 4, 4, 4, 5, 5, 7, 9] is 2.0
        engine = StatEngine([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(engine.get_std_dev(is_sample=False), 2.0)