# This package exists for compatibility with previous releases
# of ScientificPython that supported both NumPy and the old
# Numeric package. Please don't use it in new code, use numpy
# directly.

import numpy as np
import numpy.oldnumeric as on


class array(object):
    def __init__(self, *args, **kw):
        self._np = np.array(*args, **kw)
        self._on = on.array(*args, **kw)
        assert (self._np == self._on).all()
    
    def __getattr__(self, name):
        def _check(_np, _on):
            if isinstance(_np, np.ndarray):
                assert (_np == _on).all()
                
                # Hack around the constructor
                _ar = array([1])
                _ar._np = _np
                _ar._on = _on
                
                return _ar
            else:
                assert _np == _on
                return _np
        
        def fn(*args, **kw):
            _np = getattr(self._np, name)(*args, **kw)
            _on = getattr(self._on, name)(*args, **kw)
            
            return _check(_np, _on)
            
        if callable(getattr(self._np, name))
            return fn
        else:
            _np = getattr(self._np, name)
            _on = getattr(self._on, name)
            
            return _check(_np, _on)


from numpy import (
    logical_and, logical_or, less_equal, sum, arange,
    zeros, sqrt, minimum, arccos, maximum, exp, add, argsort,
    multiply, fabs, concatenate, divide, argmax, take, repeat,
    identity,
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
