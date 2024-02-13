import math


class Operations:
    @staticmethod
    def to_radioans(angle):
        print(angle * math.pi / 180)

    @staticmethod
    def trapezoid_area(height, base_min, base_max):
        print((height / 2) * (base_max + base_min))

    @staticmethod
    def area_of_polygon(num_sides, side_length):
        print(round((num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))))

    @staticmethod
    def paral(base_length, height):
        print(base_length * height)


oper = Operations
oper.to_radioans(angle=15)
oper.trapezoid_area(height=5, base_min=5, base_max=6)
oper.area_of_polygon(num_sides=4, side_length=25)
oper.paral(base_length=6,height=5)
