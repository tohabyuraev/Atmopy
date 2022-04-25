from typing import Union

from .data import Data
from .atmo import libatmopy


data = Data()


def d(
    h: Union[float, int]):
    """
    Функция возвращает значение плотности воздуха
        на высоте h (геометрическая высота) от поверхности Земли.
        Значения по ГОСТ 4401-81. Атмосфера стандартная. Параметры 

    Parameters
    ----------
    h: float, int
        Высота от поверхности Земли

    Returns
    -------
    float
        Значение плотности воздуха
    """
    if not isinstance(h, (float, int)):
        raise TypeError('Тип переменной h должен быть float или int')
    if h < 0:
        raise ValueError('Переменная h меньше нуля')
    return libatmopy.interp(
        h,
        data.d_line,
    )


def a(
    h: Union[float, int]):
    """
    Функция возвращает значение скорости звука
        на высоте h (геометрическая высота) от поверхности Земли.
        Значения по ГОСТ 4401-81. Атмосфера стандартная. Параметры 

    Parameters
    ----------
    h: float, int
        Высота от поверхности Земли

    Returns
    -------
    float
        Значение скорости звука
    """
    if not isinstance(h, (float, int)):
        raise TypeError('Тип переменной h должен быть float или int')
    if h < 0:
        raise ValueError('Переменная h меньше нуля')
    return libatmopy.interp(
        h,
        data.a_line,
    )


def g(
    h: Union[float, int]):
    """
    Функция возвращает значение ускорения свободного падения
        на высоте h (геометрическая высота) от поверхности Земли.
        Значения по ГОСТ 4401-81. Атмосфера стандартная. Параметры 

    Parameters
    ----------
    h: float, int
        Высота от поверхности Земли

    Returns
    -------
    float
        Значение ускорения свободного падения
    """
    if not isinstance(h, (float, int)):
        raise TypeError('Тип переменной h должен быть float или int')
    if h < 0:
        raise ValueError('Переменная h меньше нуля')
    return libatmopy.interp(
        h,
        data.g_line,
    )


def p(
    h: Union[float, int]):
    """
    Функция возвращает значение давления воздуха
        на высоте h (геометрическая высота) от поверхности Земли.
        Значения по ГОСТ 4401-81. Атмосфера стандартная. Параметры 

    Parameters
    ----------
    h: float, int
        Высота от поверхности Земли

    Returns
    -------
    float
        Значение давления воздуха
    """
    if not isinstance(h, (float, int)):
        raise TypeError('Тип переменной h должен быть float или int')
    if h < 0:
        raise ValueError('Переменная h меньше нуля')
    return libatmopy.interp(
        h,
        data.p_line,
    )


def t(
    h: Union[float, int]):
    """
    Функция возвращает значение температуры воздуха
        на высоте h (геометрическая высота) от поверхности Земли.
        Значения по ГОСТ 4401-81. Атмосфера стандартная. Параметры 

    Parameters
    ----------
    h: float, int
        Высота от поверхности Земли

    Returns
    -------
    float
        Значение температуры воздуха
    """
    if not isinstance(h, (float, int)):
        raise TypeError('Тип переменной h должен быть float или int')
    if h < 0:
        raise ValueError('Переменная h меньше нуля')
    return libatmopy.interp(
        h,
        data.t_line,
    )
