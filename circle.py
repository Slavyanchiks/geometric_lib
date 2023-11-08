import math

def area(r):
    '''
    Реализует нахождение площади круга с радиусом r

        Параметры:
            r (int, float, etc) : величина радиуса окружности, r >= 0

        Возвращаемое знчение:
            area (float, etc) : площадь данного круга

    input >> 2
    output >> 12.566370614359172
    '''
    if type(r) not in [int, float] :
        raise TypeError("Arguments should be int or float type")
    if r < 0 :
        raise ValueError("Radius cannot be negative")

    try :
        return math.pi * r * r
    except:
        raise "Undefined exception"


def perimeter(r):
    '''
    Реализует подсчёт длины окружности с радиусом r

        Параметры:
            r (int, float, etc) : величина радиуса окружности, r >= 0

        Возвращаемое значение:
            perimeter (float, etc) : длина окружности радиуса r

    input >> 3
    output >> 18.84955592153876
    '''
    if type(r) not in [int, float]:
        raise TypeError("Arguments should be int or float type")
    if r < 0:
        raise ValueError("Radius cannot be negative")

    try:
        return 2 * math.pi * r
    except:
        raise "Undefined exception"

