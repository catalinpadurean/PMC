import os
import PyInstaller.__main__

# Has to be called from flask-with-files dir.
PyInstaller.__main__.run(
    [
        "--name=flask-with-files",
        f"--add-data=templates{os.pathsep}templates",
        f"--add-data=static{os.pathsep}static",
        "main.py",
    ]
)
