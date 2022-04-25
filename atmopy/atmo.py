import ctypes

from .data import Line


libatmopy = ctypes.CDLL('./atmopy/libatmopy.dll', winmode=0)

libatmopy.interp.argtypes = [
    ctypes.c_float,
    ctypes.POINTER(Line),
]
libatmopy.interp.restype = ctypes.c_float
