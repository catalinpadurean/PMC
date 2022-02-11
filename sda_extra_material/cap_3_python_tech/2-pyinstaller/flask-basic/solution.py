import os
import PyInstaller.__main__

# Has to be called from flask-basic dir.
PyInstaller.__main__.run(["--name=flask-basic", "--onefile", "main.py"])
