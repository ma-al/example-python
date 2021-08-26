# Summary
Use this folder to store code that is not really being used. For example:
- you wrote some test experiments or pre-processing logic _or_
- you copied over an old messy repo that you're slowly cleaning up

Put it in here so that it is _still_ safely backed up and version-controlled.

# Notes
This folder will be pushed to the server but `pylint` will ignore anything in it, because there is no `__init__.py` file present.

For example, if you explicitly check [`bad_code.py`](./bad_code.py) like so:

```bash
cd <root_of_repo>
pylint example_python/archive/bad_code.py
```

You will get:
```
************* Module bad_code
example_python/archive/bad_code.py:7:0: C0304: Final newline missing (missing-final-newline)
example_python/archive/bad_code.py:1:0: C0114: Missing module docstring (missing-module-docstring)
example_python/archive/bad_code.py:3:0: C0103: Function name "oldFunctiontoCleanUp" doesn't conform to snake_case naming style (invalid-name)
example_python/archive/bad_code.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
example_python/archive/bad_code.py:7:4: C0103: Variable name "someVariableThatDoesNotFollowPythonStandard" doesn't conform to '[a-z0-9_]{1,30}$' pattern (invalid-name)
example_python/archive/bad_code.py:7:4: W0612: Unused variable 'someVariableThatDoesNotFollowPythonStandard' (unused-variable)

----------------------------------------------------------------------
Your code has been rated at -20.00/10 (previous run: -20.00/10, +0.00)
```

Above errors will **not** occur if instead, you simply do:

```bash
cd <root_of_repo>
pylint example_python/
```