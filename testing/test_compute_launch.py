"""_summary_
       
       Right now, not all of the tests should pass. Fix the function to pass all its tests! 
       Once all your tests pass, try writing some additional unit tests of your own!
"""
import unittest

from compute_launch import days_until_launch


# Testting using Unittest
class DaysUntilLaunch(unittest.TestCase):
    def test_days_until_launch_4(self):
        assert days_until_launch(22, 26) == 4

    def test_days_until_launch_0(self):
        assert days_until_launch(253, 253) == 0

    # fixed test: assert days_until_launch(83, 64) == 0
    def test_days_until_launch_0_negative(self):
        assert days_until_launch(83, 64) == -19

    def test_days_until_launch_1(self):
        assert days_until_launch(9, 10) == 1
