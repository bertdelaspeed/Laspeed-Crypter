import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

company_name = 'Laspeed Corp'
product_name = 'Crypto'

bdist_msi_options = {
    'upgrade_code': '{Banana-rama-30403344939493}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    }

base = None

path = sys.path
build_exe_options = {
"path": path,
"icon": "mangekyou.ico"}


if sys.platform == "win32":
    base = "Win32GUI"
    
exe = Executable(script='Crypter.py',
                 base=base,
                 icon='icones.ico',
                )

setup(  name = "Crypto",
        version = "1.0",
        description = "Encrypt and Decrypt like a boss",
        executables = [exe],
        options = {'bdist_msi': bdist_msi_options})