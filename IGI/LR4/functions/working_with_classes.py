from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
import numpy as np

class GeometricFigure(ABC): 
    def __init__(self, name):
        self._name = name
    
    @abstractmethod
    def square_figure(self):
        pass

    def get_name(self):
        return self._name

class ColorFigure:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height
        self.color_figure = ColorFigure(color)

    def square_figure(self):
        return self.width * self.height

    def get_info(self):
        return "Фигура: {0}, ширина: {1}, высота: {2}, цвет: {3}, площадь: {4:.2f}".format(
            self.get_name(), self.width, self.height, self.color_figure.color, self.square_figure()
        )

class Circle(GeometricFigure):
    def __init__(self, radius, color):
        super().__init__("Круг")
        self.radius = radius
        self.color_figure = ColorFigure(color)

    def square_figure(self):
        return math.pi * self.radius ** 2

    def get_info(self):
        return "Фигура: {0}, радиус: {1}, цвет: {2}, площадь: {3:.2f}".format(
            self.get_name(), self.radius, self.color_figure.color, self.square_figure()
        )


class Rhombus(GeometricFigure):
    def __init__(self, d1, d2, color):
        super().__init__("Ромб")
        self.d1 = d1
        self.d2 = d2
        self.color_figure = ColorFigure(color)

    def square_figure(self):
        return (self.d1 * self.d2) / 2

    def get_info(self):
        return "Фигура: {0}, диагонали: {1} и {2}, цвет: {3}, площадь: {4:.2f}".format(
            self.get_name(), self.d1, self.d2, self.color_figure.color, self.square_figure()
        )


class Square(GeometricFigure):
    def __init__(self, side, color):
        super().__init__("Квадрат")
        self.side = side
        self.color_figure = ColorFigure(color)

    def square_figure(self):
        return self.side ** 2

    def get_info(self):
        return "Фигура: {0}, сторона: {1}, цвет: {2}, площадь: {3:.2f}".format(
            self.get_name(), self.side, self.color_figure.color, self.square_figure()
        )


class Triangle(GeometricFigure):
    def __init__(self, base, height, color):
        super().__init__("Треугольник")
        self.base = base
        self.height = height
        self.color_figure = ColorFigure(color)

    def square_figure(self):
        return 0.5 * self.base * self.height

    def get_info(self):
        return "Фигура: {0}, основание: {1}, высота: {2}, цвет: {3}, площадь: {4:.2f}".format(
            self.get_name(), self.base, self.height, self.color_figure.color, self.square_figure()
        )


class RegularPolygon(GeometricFigure):
    def __init__(self, n, a, color):
        if n < 3:
            raise ValueError("У правильного многоугольника должно быть минимум 3 стороны.")
        super().__init__(f"Правильный {n}-угольник")
        self.n = n
        self.a = a
        self.color_figure = ColorFigure(color)

    def square_figure(self):
        return (self.n * self.a ** 2) / (4 * math.tan(math.pi / self.n))

    def get_info(self):
        return "Фигура: {0}, количество сторон: {1}, длина стороны: {2}, цвет: {3}, площадь: {4:.2f}".format(
            self.get_name(), self.n, self.a, self.color_figure.color, self.square_figure()
        )
    
    def draw(self, filename, label=""):
        angles = np.linspace(0, 2 * np.pi, self.n, endpoint=False)
        
        x = self.a * np.cos(angles)
        y = self.a * np.sin(angles)
        
        x = np.append(x, x[0])  
        y = np.append(y, y[0])
        
        fig, ax = plt.subplots()
        ax.fill(x, y, self.color_figure.color)  
        
        ax.text(0, 0, label, ha='center', va='center', fontsize=12, color='black')

        plt.savefig(filename)
        plt.show()
        plt.close()
