from contextlib import contextmanager
import datetime
import sys
import time

from .pretty_time import pretty_time

def delay(seconds, report_seconds=10, out=sys.stdout, string="process"):
  """
  Blocks and delays execution while printing useful information
  Will wait print out time to go every report_seconds
  """
  seconds = int(seconds)
  report_seconds = int(report_seconds)

  stop_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

  def info():
    seconds_left = (stop_time - datetime.datetime.now()).total_seconds()

  while True:
    seconds_left = (stop_time - datetime.datetime.now()).total_seconds()
    if seconds_left > 0.1:
      out.write("Delaying {} for {} seconds to run at {}\n".format(string, round(seconds_left), stop_time.strftime("%c")))
    else:
      out.write("Finished waiting for {} at {}\n".format(string, datetime.datetime.now().strftime("%c")))
      break

    seconds_to_wait = seconds_left % report_seconds

    if seconds_to_wait < 0.1:
      seconds_to_wait += report_seconds
    seconds_to_wait = min(seconds_to_wait, seconds_left)
    time.sleep(seconds_to_wait)
