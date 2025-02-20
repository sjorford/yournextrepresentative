import sys
from io import StringIO
from contextlib import contextmanager


@contextmanager
def capture_output():
    # Suggested here: http://stackoverflow.com/a/17981937/223092
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield new_out, new_err
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def split_output(stringio_output):
    return stringio_output.getvalue().strip().splitlines()
