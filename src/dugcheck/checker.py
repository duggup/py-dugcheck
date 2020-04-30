# encoding=utf-8
import logging
from inspect import getfullargspec
from flask import Flask


logger = logging.getLogger(__name__)


class Dugcheck(object):
    """Function is a wrap over standard python function

    An instance of this Function class is also callable
    just like the python function that it wrapped.
    When the instance is "called" like a function it fetches
    the function to be invoked from the virtual namespace and then
    invokes the same.
    """

    def __init__(self, fn):
        self.fn = fn
        self.flask = Flask(__name__)

    def question(self, fn):
        """Wrapper.
        """
        if args is None:
            args = getfullargspec(self.fn).args

        return (
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
        )

    def run(self, host="0.0.0.0", port="3002"):
        self.flask.run(host=host, port=port)
