import math


def circle_properties(radius):
    circumference = 2 * math.pi * radius  e
    area = math.pi * radius ** 2  
    return circumference, area


def triangle_area(base, height):
    area = 0.5 * base * height  
    return area


def rectangle_area(length, width):
    area = length * width  
    return area


radius = 5  
base = 6  
height = 4  
length = 8  
width = 3  


circle_circumference, circle_area = circle_properties(radius)
triangle_area_value = triangle_area(base, height)
rectangle_area_value = rectangle_area(length, width)