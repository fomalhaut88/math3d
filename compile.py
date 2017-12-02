from pycdll.compiler import Compiler

cpl = Compiler(
    c_dir='c',
    dll_dir='math3d/dll'
)
cpl.compile('math3d')
