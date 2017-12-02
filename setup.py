from distutils.core import setup
from pycdll.compiler import Compiler

cpl = Compiler(
    c_dir='c',
    dll_dir='math3d/dll'
)

print("compiling C libraries...")
cpl.compile('math3d')

package_data = {
    'math3d': ['dll/' + cpl.get_dllname('math3d')]
}

setup(
    name='math3d',
    version='1.0',
    packages=['math3d'],
    license="",
    long_description=open('README.md').read(),
    package_data=package_data
)
