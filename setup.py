from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "includes": ["src"]}

# base="Win32GUI" should be used only for Windows GUI app
"""base = None
if sys.platform == "win32":
    base = "Win32GUI"
"""

exe = Executable(
    script="src/observer.py",
    copyright="Copyright (C) 2021 Organization-folder",
    base="Win32GUI",
    icon="icon.ico",
    shortcutName="Organization Folder",
    shortcutDir="OrganizationFolder",
)

setup(
    name="App-organization-folder",
    version="0.0.2",
    description="App-organization-folder",
    author="Gabriel Terra",
    options={"biuld_exe": build_exe_options},
    executables=[exe]
)
