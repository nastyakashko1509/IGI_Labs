import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

class PowerSeriesExpansion:

    def power_series_expansion(self, x, eps):
        """  Функция для вычисления разложения функции в ряд по степеням x с заданной точностью.  """
    
        if x > 1 or x < -1 or eps < 0 or eps > 1:
            print("Неверный диапазон или недопустимая погрешность!")
            return None
    
        result = math.pi / 2

        for i in range(250):
            term = (math.factorial(2 * i) * x ** (2 * i + 1)) / (4 ** i * (math.factorial(i)) ** 2 * (2 * i + 1))

            if abs(term) <= eps:
                return result

            result -= term

        return result

    def arithmetic_mean_of_elements(self, x, eps):
        """  Функция, считающая среднее арифметическое элементов степенного ряда.  """

        if x > 1 or x < -1 or eps < 0 or eps > 1:
            print("Неверный диапазон или недопустимая погрешность!")
            return None
    
        result = math.pi / 2
        count_elem = 1

        for i in range(250):
            term = (math.factorial(2 * i) * x ** (2 * i + 1)) / (4 ** i * (math.factorial(i)) ** 2 * (2 * i + 1))

            if abs(term) <= eps:
                return result / count_elem

            count_elem += 1
            result -= term

        return result / count_elem
    
    def median_of_elements(self, x, eps):
        """  Функция, считающая медиану элементов степенного ряда.  """

        if x > 1 or x < -1 or eps < 0 or eps > 1:
            print("Неверный диапазон или недопустимая погрешность!")
            return None
    
        mass_elem = []
        mass_elem.append(math.pi / 2)

        for i in range(250):
            term = (math.factorial(2 * i) * x ** (2 * i + 1)) / (4 ** i * (math.factorial(i)) ** 2 * (2 * i + 1))
            
            if abs(term) <= eps:
                break

            mass_elem.append(term)

        mass_elem.sort()

        if len(mass_elem) > 2:
            if len(mass_elem) % 2 == 1:
                return mass_elem[len(mass_elem) // 2]
            else:
                mid = len(mass_elem) // 2
                return (mass_elem[mid + 1] + mass_elem[mid]) / 2
        else:
            if len(mass_elem) == 1:
                return mass_elem[0]
            else:
                return (mass_elem[0] + mass_elem[1]) / 2
        
    def mode_of_elements(self, x, eps):
        """  Функция, считающая моду элементов степенного ряда.  """

        if x > 1 or x < -1 or eps < 0 or eps > 1:
            print("Неверный диапазон или недопустимая погрешность!")
            return None
    
        mass_elem = []
        mass_elem.append(math.pi / 2)

        for i in range(250):
            term = (math.factorial(2 * i) * x ** (2 * i + 1)) / (4 ** i * (math.factorial(i)) ** 2 * (2 * i + 1))
            
            if abs(term) <= eps:
                break

            mass_elem.append(term)

        counts = Counter(mass_elem)
        max_count = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_count]
    
        if len(modes) == len(mass_elem):
            return None  
        return modes 

    def dispersion_of_elements(self, x, eps):
        """  Функция, считающая дисперсию элементов степенного ряда.  """

        arithmetic_mean = self.arithmetic_mean_of_elements(x, eps)
        deviation_elem = []
        deviation_elem.append(math.pi / 2 - arithmetic_mean)

        for i in range(250):
            term = (math.factorial(2 * i) * x ** (2 * i + 1)) / (4 ** i * (math.factorial(i)) ** 2 * (2 * i + 1))
            
            if abs(term) <= eps:
                break

            deviation_elem.append(term - arithmetic_mean)

        dispersion = 0
        for deviation in deviation_elem:
            dispersion += deviation ** 2

        return dispersion / len(deviation_elem)
    
    def sko_of_elements(self, x, eps):
        """  Функция, считающая ско элементов степенного ряда.  """
        
        dispersion = self.dispersion_of_elements(x, eps)
        return math.sqrt(dispersion)
    
    def plotting_function_graphs(self, eps):
        """  Функция, строящая графики функции и суммы ряда, сохраняющая их в файл.  """

        x_values = np.linspace(-1, 1, 400)
        y_series_values = [self.power_series_expansion(x, eps) for x in x_values]
        y_exact_values = np.arccos(x_values) 
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_series_values, label='Ряд Тейлора для arccos(x)', color='blue')
        plt.plot(x_values, y_exact_values, label='Точная функция arccos(x)', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График разложения функции arccos(x) и точной функции')
        plt.legend()
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.savefig('D:\\IGI_Labs\\IGI\\LR4\\file_work\\arccos_expansion_plot.png')

        return None
    
    def power_series_expansion_result(self, x, eps):
        print("arccos(x) = ", self.power_series_expansion(x, eps))
        print("Среднее значение всех элементов суммы ряда: ", self.power_series_expansion(x,eps))
        print("Медиана всех элементов суммы ряда: ", self.median_of_elements(x, eps))
        print("Мода всех элементов суммы ряда: ", self.mode_of_elements(x, eps))
        print("Дисперсия всех элементов суммы ряда: ", self.dispersion_of_elements(x, eps))
        print("СКО всех элементов суммы ряда: ", self.sko_of_elements(x, eps))
        self.plotting_function_graphs(eps)

        return None
    