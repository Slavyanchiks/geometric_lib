def area(a, h):
    '''
    Реализует подсчёт площади треугольника со стороной a, и высотой, опущенной на эту сторону h

        Параметры:
            a (int, float, etc) : длина стороны треугольника, a >= 0
            h (int, float, etc) : длина высоты треугольника, опущенной на эту сторону, h >= 0

        Возвращаемое значение:
            area (int, float, etc) : площадь данного треугольника

    input >> 3, 4
    output >> 6
    '''
    if any((param not in [int, float]) for param in [type(a), type(h)]) :
        raise TypeError("Arguments should be int or float type")
    if any(param < 0 for param in [a, h]):
        raise ValueError("Sides' length cannot be negative")

    try :
        return a * h / 2
    except:
        raise "Undefined exception"

def perimeter(a, b, c):
    '''
    Реализует нахождение периметра для треугольника со сторонами a, b, c

        Параметры:
            a, b, c (int, float, etc) : соответственные стороны треугольника, a,b,c >= 0

        Возвращаемое значение:
            perimeter (int, float, etc) : периметр треугольника

    input >> 3, 4, 5
    output >> 12
    '''
    if any((param not in [int, float]) for param in [type(a), type(b), type(c)]):
        raise TypeError("Arguments should be int or float type")
    if any(param < 0 for param in [a, b, c]):
        raise ValueError("Sides' length cannot be negative")

    try:
        return a + b + c
    except :
        raise "Undefined exception"