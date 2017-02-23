import sys

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["lxml", "requests", "gzip", "os"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="EcustNet",
    version="0.1",
    description="Auto Login for the Net in Ecust Campus",
    options={'build_exe': build_exe_options},
    executables=[Executable("gui.py", base=base), Executable("core.py", base=base)]
)
