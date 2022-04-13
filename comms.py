import functools
import os
import pathlib
import pickle
import sys
from collections import Callable

import requests


class Server:
    def __init__(self, baseurl: str):
        self._baseurl = baseurl

    def call(self, func: Callable) -> Callable:
        """Decorate a function to run on the server."""
        if os.environ.get("I_AM_SERVER"):
            return func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            url = (
                self._baseurl + "?func=" + func.__name__ + "&module=" + func.__module__
            )
            if "__main__" in sys.modules:
                url += "&main=" + pathlib.Path(sys.modules["__main__"].__file__).stem
            data = pickle.dumps((args, kwargs))
            result = requests.post(url, data)
            return pickle.loads(result.content)

        return wrapped
