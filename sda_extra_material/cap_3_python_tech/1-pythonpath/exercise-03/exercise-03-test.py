r"""
>>> import os
>>> import sys
>>> import subprocess

>>> if os.getenv("PYTHONPATH") is None:
...    os.environ["PYTHONPATH"] = os.path.abspath("../exercise-01")

>>> exercise = subprocess.Popen([sys.executable, "exercise-03.py"], shell=True, stdout=subprocess.PIPE)
>>> out, _ = exercise.communicate()
>>> exercise.returncode
0
>>> "Success" in out.decode()
True
"""
