from cx_Freeze import setup,Executable

includes = ["tri"]

exe = Executable(
  script="game.py",
  base= None,
  copyDependentFiles = True,
  targetName = "triominos.exe")

setup(version="1.0",options={"build_exe":{"includes":includes}},executables = [exe])