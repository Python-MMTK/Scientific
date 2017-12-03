# This package exists for compatibility with previous releases
# of ScientificPython that supported both NumPy and the old
# Numeric package. Please don't use it in new code, use numpy
# directly.

import numpy as np

from numpy import array, logical_and
from numpy import array_equal as equal

def int_sum(a, axis=0):
    return np.add.reduce(a, axis)
def zeros_st(shape, other):
    return np.zeros(shape, dtype=other.dtype)
from numpy import ndarray as array_type
package = "NumPy"
