#!/usr/bin/env python

import os
import sys
import platform
import pkginfo
import numpy.distutils.misc_util
import textwrap

from setuptools import setup
from glob import glob

from distutils.core import Extension
from distutils.command.install_headers import install_headers
from Cython.Build import cythonize
from numpy.distutils.system_info import default_include_dirs, default_lib_dirs

use_cython = True
src_ext = 'pyx'

cmdclass = {}
extra_compile_args = ["-DNUMPY=1"]
numpy_include = []
data_files = []
scripts = []
options = {}
is_py3 = False

numpy_include = numpy.distutils.misc_util.get_numpy_include_dirs()

math_libraries = []
if sys.platform != 'win32':
    math_libraries.append('m')


ext_modules = [Extension('Scientific._netcdf',
                            ['Scientific/_netcdf.c'],
                            include_dirs=(
                                numpy_include + default_include_dirs +
                                ['Include']
                            ),
                            library_dirs=default_lib_dirs,
                            libraries = ['netcdf'],
                            extra_compile_args=extra_compile_args)]

packages = ['Scientific', 'Scientific.Clustering', 'Scientific.Functions',
            'Scientific.Geometry', 'Scientific.IO',
            'Scientific.Physics', 'Scientific.QtWidgets',
            'Scientific.Statistics', 'Scientific.Signals',
            'Scientific.Threading', 'Scientific.TkWidgets',
            'Scientific.Visualization', 'Scientific.MPI',
            'Scientific.DistributedComputing']

ext_modules.append(Extension('Scientific._vector',
                             ['Scientific/_vector.%s' % src_ext],
                             include_dirs=['Include']+numpy_include,
                             libraries=math_libraries,
                             extra_compile_args=extra_compile_args))
ext_modules.append(Extension('Scientific._affinitypropagation',
                             ['Scientific/_affinitypropagation.%s' % src_ext],
                             include_dirs=['Include']+numpy_include,
                             libraries=math_libraries,
                             extra_compile_args=extra_compile_args))
ext_modules.append(Extension('Scientific._interpolation',
                             ['Scientific/_interpolation.%s' % src_ext],
                             include_dirs=['Include']+numpy_include,
                             libraries=math_libraries,
                             extra_compile_args=extra_compile_args))

scripts.append('task_manager')
if sys.version[:3] >= '2.1':
    packages.append('Scientific.BSP')
    scripts.append('bsp_virtual')

headers = glob(os.path.join ("Include","Scientific","*.h"))
# headers.append(netcdf_h_file)

setup (name = "ScientificPython",
       version = "2.6.2",
       description = "Various Python modules for scientific computing",
       long_description = 
"""ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.""",
       author = "Konrad Hinsen",
       author_email = "hinsen@cnrs-orleans.fr",
       url = "http://dirac.cnrs-orleans.fr/ScientificPython/",
       license = "CeCILL-C",

       packages = packages,
       ext_modules = cythonize(ext_modules),
       scripts = scripts,
       data_files = data_files,
       headers = headers,
       cmdclass = cmdclass,
       options = options,
       use_2to3 = True,
       install_requies=[
           'numpy>=1.6',
           'oldnumeric',
       ],
       )
