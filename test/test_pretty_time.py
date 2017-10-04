import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ticktock import pretty_time


class TestPrettyTime(unittest.TestCase):
  def test_pretty_time(self):
    assert pretty_time(123) == '2m3s'
    assert pretty_time(12345) == '3h25m45s'
    assert pretty_time(1234567) == '14d6h56m7s'

if __name__ == '__main__':
  unittest.main()
