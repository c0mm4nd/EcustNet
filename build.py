from cx_Freeze import setup, Executable

setup(
    name="EcustNet",
    version="0.1",
    description="Auto Login for the Net in Ecust Campus",
    executables=[Executable("gui.py")]
)
