import math

def power_series_expansion(x, eps):
    """  Функция для вычисления разложения функции в ряд по степеням x с заданной точностью.  """
    
    if x > 1 or x < -1 or eps < 0 or eps > 1:
        print("Неверный диапазон или недопустимая погрешность!")
        return None
    
    result = math.pi / 2

    for i in range(500):
        term = (math.factorial(2 * i) * x ** (2 * i + 1)) / (4 ** i * (math.factorial(i)) ** 2 * (2 * i + 1))

        if abs(term) <= eps:
            return result

        result -= term

    return result