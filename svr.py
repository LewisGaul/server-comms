import importlib
import os
import pickle
import sys

import flask

app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def route():
    main_module = flask.request.args.get("main")
    module_name = flask.request.args.get("module")
    func_name = flask.request.args.get("func")
    if main_module and main_module != "__main__":
        print(f"Setting {main_module!r} as __main__ and importing")
        sys.modules["__main__"] = importlib.import_module(main_module)
    print(f"Importing {module_name!r}")
    module = importlib.import_module(module_name)
    data = flask.request.get_data()
    args, kwargs = pickle.loads(data)
    print(f"Running {module_name}.{func_name}() with {args}, {kwargs}")
    result = getattr(module, func_name)(*args, **kwargs)
    return pickle.dumps(result)


if __name__ == "__main__":
    os.environ["I_AM_SERVER"] = "1"
    app.run("0.0.0.0", "8000", debug=True)
