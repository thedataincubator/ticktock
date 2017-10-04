from contextlib import contextmanager
import datetime
import sys

from .pretty_time import pretty_time

@contextmanager
def timer(out=sys.stdout):
  start = datetime.datetime.now()
  yield
  end = datetime.datetime.now()
  out.write("Seconds elapsed: {}\n".format(pretty_time((end - start).total_seconds())))
