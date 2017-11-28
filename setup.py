from distutils.core import setup
from setuptools import find_packages
from pycdll.compiler import Compiler

cpl = Compiler(
    c_dir='c',
    dll_dir='dll'
)

print("compiling C libraries...")
for clib in cpl.get_clibs():
    cpl.compile(clib)

data_files = [
    ('dll', cpl.collect_local_dlls()),
]

setup(
    name='math3d',
    version='1.0',
    packages=find_packages(),
    license="",
    long_description=open('README.md').read(),
    data_files=data_files
)
