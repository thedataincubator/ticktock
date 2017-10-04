import os
import sys
import time
import unittest
from StringIO import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ticktock import timer


class TestPrettyTime(unittest.TestCase):
  def test_pretty_time(self):
    buffer = StringIO()
    with timer(out=buffer):
      time.sleep(2)
    assert "Seconds elapsed: 2s" in buffer.getvalue()

if __name__ == '__main__':
  unittest.main()
