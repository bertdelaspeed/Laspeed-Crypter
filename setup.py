import os
import sys
from cx_Freeze import setup, Executable
#import cx_Freeze

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

#executables = [cx_Freeze.Executable("Crypter.py", base=None)]

exe =Executable(
        script = "Crypter.py",
        icon = "mangekyou.ico",
        targetName = "Crypter.exe",
        base = base
        )

includefiles = ["mangekyou.ico"]

# cx_Freeze.setup(
#
#     name="Encrypt Decrypt",
#     options={"build_exe": {"packages": ["numpy"]}},
#     version = "0.01",
#     descriptions = "Trying to get this to work",
#     executables = executables
#
# )
setup(
    name = "Encrypt Decrypt",
    version = "1.0",
    description = "Encrypt and Decrypt messages using this amazing application",
    author = "Wilfried Bertrand Aka LASPEED",
    author_email="bertdelaspeed@gmail.com",
    options = {'build_exe': {'include_files':includefiles}},
    executables = [exe]
)
