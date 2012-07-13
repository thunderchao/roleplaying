from cx_Freeze import setup, Executable

exe = Executable(
    script="wrapper.py",
    base="Win32GUI",
    compress = True,
    )

setup(
    name = "D&D Tools",
    author = "Nathaniel Ray Pickett",
    version = "1.0",
    description = "Set of tools for running a D&D session",
    executables = [exe]
    )
