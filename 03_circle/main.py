import math


class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def find_square(self):
        return round(math.pi * self.radius ** 2, 4)

    def find_perimeter(self):
        return round(math.pi * 2 * self.radius, 4)

    def enlargement(self, value):
        self.radius += value

    def print_info(self):
        print(f'\nОкружность с координатами x = {self.x}; y = {self.y}\nРадиус: {self.radius}\n'
              f'Площадь круга:{self.find_square()}\nПериметр круга: {self.find_perimeter()}')

    def is_intersection(self, second_circle):
        if not isinstance(second_circle, Circle):
            print('Окружность не найдена!')
        else:
            distance_between_centers_of_circles = math.sqrt(
                (second_circle.x - self.x) ** 2 + (second_circle.y - self.y) ** 2
            )
            if distance_between_centers_of_circles > self.radius + second_circle.radius:
                return False
            else:
                return True


cir1 = Circle(2, 3, 1)
cir2 = Circle(0, 2, 1)

cir1.print_info()
cir2.print_info()
print(cir2.is_intersection(cir1))
