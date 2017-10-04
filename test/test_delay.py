import os
import sys
import time
import unittest
from StringIO import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ticktock import delay


class TestDelay(unittest.TestCase):
  def test_delay(self):
    buffer = StringIO()
    delay(5,2,out=buffer)
    results = buffer.getvalue()
    assert "Delaying 5.0 seconds" in results
    assert "Delaying 4.0 seconds" in results
    assert "Delaying 2.0 seconds" in results
    assert "Finished waiting" in results

if __name__ == '__main__':
  unittest.main()
