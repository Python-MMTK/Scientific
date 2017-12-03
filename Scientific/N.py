# This package exists for compatibility with previous releases
# of ScientificPython that supported both NumPy and the old
# Numeric package. Please don't use it in new code, use numpy
# directly.

import numpy as np

from numpy import (
    array, logical_and, logical_or, less_equal, sum, arange,
    zeros, sqrt, minimum, arccos, maximum, exp, add, argsort,
    multiply, fabs, concatenate, divide
)
from numpy import array_equal as equal
from numpy import conj as conjugate
from numpy import ndarray as ArrayType
from numpy import newaxis as NewAxis
from numpy import float64 as Float
from numpy import int64 as Int

def int_sum(a, axis=0):
    return np.add.reduce(a, axis)
def zeros_st(shape, other):
    return np.zeros(shape, dtype=other.dtype)
from numpy import ndarray as array_type
package = "NumPy"
