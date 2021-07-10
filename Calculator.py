# # ### Create a class called Calculator
# # - functions, practice using, defining and calling functions
#
# # Build a basic functional
# # ## Core 1: build function containing
#     # add,
#     # subtract,
#     # multiply,
#     # divide.
#
# # Create a file for child class called Functional_calculator
# # import calculator class and inherit all the functionality
# # ## Core 2: Build more functions for
#     # area of a circle
#     # area of a square
#     # area of a triangle (just find the easiest way)
#
# class Calculator():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         return self.a + self.b
#
#     def subtraction(self):
#         return self.a - self.b
#
#     def multiplication(self):
#         return self.a * self.b
#
#     def division(self):
#         return int(self.a / self.b)
#
# cal= Calculator(10,2)
#
# print(cal.addition())
# print(cal.subtraction())
# print(cal.multiplication())
# print(cal.division())



# ### Core 2
import math
class Area_Calculator():
    def __init__(self,l,w,h,r):
        self.length = l
        self.width = w
        self.height = h
        self.radius = r


    def area_circle(self):
        return self.radius * self.ra * math.pi

    def area_square(self):
        return self.length * self.width

    def area_triange(self):
        return (self.height * self.length)/2


# l,w,h,r
cal = Area_Calculator(10,5,0,0)
print(cal.area_square())