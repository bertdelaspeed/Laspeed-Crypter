
import sys
import os
from cx_Freeze import Executable, setup


os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

company_name = 'Laspeed Corp'
product_name = 'Crypto'

bdist_msi_options = {
    'upgrade_code': '{Banana-rama-30403344939493}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    }

path = sys.path
base = None
if sys.platform == "win32":
   base = 'Win32GUI'

exe = Executable(
        script = "Crypter.py",
        icon = "mangekyou.ico",
        targetName = "Crypter.exe",
        base = base
        )

build_exe_options = {'packages':['webbrowser', 'tkinter','PIL'], 'include_files':['face.jpg', 'linkd.png', 'icones.ico'],'icon':['mangekyou.ico']}


setup(
  name='Crypter',
  version='1.0',
  description='Hackers secret communication tool',
  author = "Wilfried Bertrand Aka LASPEED",
  author_email="bertdelaspeed@gmail.com",
  options = {'build.exe':build_exe_options,'bdist_msi': bdist_msi_options},
  executables = [exe]
  )