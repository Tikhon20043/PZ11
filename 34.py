# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота".
# От этого класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Figure:
    def __init__(self, width, height):
        self.width = width # Установка ширины фигуры
        self.height = height # Установка высоты фигуры

    def get_area(self):
        return self.width * self.height # Вычисление площади

    def get_perimeter(self):
        return 2 * (self.width + self.height) # Вычисление периметра

class Rectangle(Figure):
    pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def get_area(self):
        return self.width ** 2 #  Вычисляет площадь квадрата

    def get_perimeter(self):
        return 4 * self.width # Вычисляет периметр квадрата

rectangle = Rectangle(5, 10) # Создание прямоугольника
square = Square(7) # Создание квадрата

print("Прямоугольник:")
print(f"Площадь: {rectangle.get_area()}")
print(f"Периметр: {rectangle.get_perimeter()}")

print("\nКвадрат:")
print(f"Площадь: {square.get_area()}")
print(f"Периметр: {square.get_perimeter()}")