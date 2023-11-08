def area(a, b):
    '''
    Реализует подсчёт площади прямоугольника со сторонами a и b

        Параметры:
            a, b (int, float, etc) :  соответствующие стороны прямоугольника, a,b >= 0

        Возвращаемое значение:
            area (int, float, etc) : площадь прямоугольника

    input >> 2,3
    output >> 6
    '''
    if any((param not in [int, float]) for param in [type(a), type(b)]) :
        raise TypeError("Arguments should be int or float type")
    if any(param < 0 for param in [a, b]):
        raise ValueError("Sides' length cannot be negative")

    try :
        return a * b
    except:
        raise "Undefined exception"

def perimeter(a, b):
    '''
    Реализует подсчёт периметра прямоугольника со сторонами a, b

        Параметры:
            a, b (int, float, etc) : соответствующие стороны прямоугольника, a,b >= 0

        Возвращаемое значение:
            perimeter (int, float, etc) : периметр прямоугольника

    input >> 3.5, 4.5
    output >> 16.0
    '''
    if any((param not in [int, float]) for param in [type(a), type(b)]):
        raise TypeError("Arguments should be int or float type")
    if any(param < 0 for param in [a, b]):
        raise ValueError("Sides' length cannot be negative")

    try:
        return 2*(a * b)
    except:
        raise "Undefined exception"