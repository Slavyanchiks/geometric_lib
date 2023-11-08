
def area(a):
    '''
    Реализует подсчёт площади квадрата со стороной a

        Параметры:
            a (int, float, etc) : длина стороны квадрата, a >= 0

        Возвращаемое значение:
            area (int, float, etc) : площадь квадрата

    input >> 3.5
    output >> 12.25
    '''
    if type(a) not in [int, float]:
        raise TypeError("Arguments should be int or float type")
    if a < 0:
        raise ValueError("Sides' length cannot be negative")

    try:
        return a * a
    except:
        raise "Undefined exception"


def perimeter(a):
    '''
    Реализует нахождение периметра квадрата

        Парметры:
            a (int, float, etc) : длина стороны квадрата, a >= 0

        Возвращаемое значение:
            perimeter (int, float, etc) : периметр квадрата со стороной a

    input >> 3
    output >> 12
    '''
    if type(a) not in [int, float]:
        raise TypeError("Arguments should be int or float type")
    if a < 0:
        raise ValueError("Sides' length cannot be negative")

    try:
        return 4 * a
    except:
        raise "Undefined exception"
