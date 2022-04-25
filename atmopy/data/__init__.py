import ctypes


class Line(ctypes.Structure):
    _fields_ = (
        ('x', ctypes.POINTER(ctypes.c_float)),
        ('y', ctypes.POINTER(ctypes.c_float)),
        ('n', ctypes.c_size_t),
    )


class Data(object):
    def __init__(self):
        self.initialize()

        self.g_line: Line = None
        self.d_line: Line = None
        self.p_line: Line = None
        self.a_line: Line = None
        self.t_line: Line = None
        self.prepare()
        
    def initialize(self):
        with open('./atmopy/data/g.csv', 'r') as _:
            self.g_data = list(
                map(float, _.read().split(','))
            )
        with open('./atmopy/data/d.csv', 'r') as _:
            self.d_data = list(
                map(float, _.read().split(','))
            )
        with open('./atmopy/data/h.csv', 'r') as _:
            self.h_data = list(
                map(float, _.read().split(','))
            )
        with open('./atmopy/data/p.csv', 'r') as _:
            self.p_data = list(
                map(float, _.read().split(','))
            )
        with open('./atmopy/data/a.csv', 'r') as _:
            self.a_data = list(
                map(float, _.read().split(','))
            )
        with open('./atmopy/data/t.csv', 'r') as _:
            self.t_data = list(
                map(float, _.read().split(','))
            )

    def prepare(self):
        n = len(self.a_data)

        self.g_line = Line(
            (ctypes.c_float * n)(*self.h_data),
            (ctypes.c_float * n)(*self.g_data),
            ctypes.c_size_t(n),
        )
        self.d_line = Line(
            (ctypes.c_float * n)(*self.h_data),
            (ctypes.c_float * n)(*self.d_data),
            ctypes.c_size_t(n),
        )
        self.p_line = Line(
            (ctypes.c_float * n)(*self.h_data),
            (ctypes.c_float * n)(*self.p_data),
            ctypes.c_size_t(n),
        )
        self.a_line = Line(
            (ctypes.c_float * n)(*self.h_data),
            (ctypes.c_float * n)(*self.a_data),
            ctypes.c_size_t(n),
        )
        self.t_line = Line(
            (ctypes.c_float * n)(*self.h_data),
            (ctypes.c_float * n)(*self.t_data),
            ctypes.c_size_t(n),
        )
