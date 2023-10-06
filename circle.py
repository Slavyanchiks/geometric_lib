import math

def area(r):
    '''
    Реализует нахождение площади круга с радиусом r

        Параметры:
            r (int, float, etc) : величина радиуса окружности

        Возвращаемое знчение:
            area (int, float, etc) : площадь данного круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Реализует подсчёт длины окружности с радиусом r

        Параметры:
            r (int, float, etc) : величина радиуса окружности

        Возвращаемое значение:
            perimeter (int, float, etc) : длина окружности радиуса r
    '''
    return 2 * math.pi * r

