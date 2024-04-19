# Простой уровень:
# 1) Создайте класс Car, который имеет атрибуты make (марка) и model (модель).
# Реализуйте метод display_info(), который выводит информацию о марке и модели автомобиля.


# class Car:
#     def __init__(self, make: str, model: str):
#         self.make = make
#         self.model = model
#
#     def display_info(self):
#         print(f'make: {self.make}, model: {self.model}')
#
# car1 = Car(make='Mercedes', model='m32')
#
# car1.display_info()

# 2) Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
# Реализуйте метод calculate_area(), который возвращает площадь прямоугольника.


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

kvadrat = Rectangle(width=16, height=16)
rectangle1 = Rectangle(width=176, height=32)
print(kvadrat.calculate_area())
print(rectangle1.calculate_area())

