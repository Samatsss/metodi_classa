# задание 1


# class Passport():
#     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.country = country
#         self.numb_of_pasport = numb_of_pasport
#
#     def PrintInfo(self):
#         print("\nFullname: ", self.first_name, " ", self.last_name)
#         print("Date of birth: ", self.date_of_birth)
#         print("County: ", self.country)
#         print("Passport number: ", self.numb_of_pasport)
#
#
# class ForeignPassport(Passport):
#     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport, visa):
#         super().__init__(first_name, last_name, country, date_of_birth, numb_of_pasport)
#         self.visa = visa
#
#     def PrintInfo(self):
#         super().PrintInfo()
#         print("Visa: ", self.visa)
#
# class PassportList:
#     def __init__(self):
#         self.passports = []
#
#     def add_passport(self, passport):
#         self.passports.append(passport)
#
#     def print_all_info(self):
#         for passport in self.passports:
#             passport.PrintInfo()
#
# passport1 = Passport("John", "Doe", "USA", "01.01.1990", "123456789")
# foreign_passport1 = ForeignPassport("Jane", "Doe", "USA", "02.02.1995", "987654321", "Tourist Visa")
#
# passport_list = PassportList()
# passport_list.add_passport(passport1)
# passport_list.add_passport(foreign_passport1)
#
# passport_list.print_all_info()




# задание 6

# import math
#
# class RightTriangle:
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2
#         self.hypotenuse = math.sqrt(side1**2 + side2**2)
#
#     def increase_side(self, percent):
#         self.side1 *= 1 + percent / 100
#         self.side2 *= 1 + percent / 100
#         self.hypotenuse = math.sqrt(self.side1**2 + self.side2**2)
#
#     def decrease_side(self, percent):
#         self.side1 *= 1 - percent / 100
#         self.side2 *= 1 - percent / 100
#         self.hypotenuse = math.sqrt(self.side1**2 + self.side2**2)
#
#     def radius_of_circumscribed_circle(self):
#         return self.hypotenuse / 2
#
#     def perimeter(self):
#         return self.side1 + self.side2 + self.hypotenuse
#
#     def angles(self):
#         angle1 = math.degrees(math.asin(self.side1 / self.hypotenuse))
#         angle2 = math.degrees(math.asin(self.side2 / self.hypotenuse))
#         angle3 = 90  # Угол между катетами
#         return angle1, angle2, angle3
#
# triangle = RightTriangle(3, 4)
# print("Original Triangle:")
# print("Side 1:", triangle.side1)
# print("Side 2:", triangle.side2)
# print("Hypotenuse:", triangle.hypotenuse)
# print("Perimeter:", triangle.perimeter())
# print("Circumscribed Circle Radius:", triangle.radius_of_circumscribed_circle())
# print("Angles:", triangle.angles())
#
# triangle.increase_side(10)
# print("\nTriangle after Increasing Side Lengths by 10%:")
# print("Side 1:", triangle.side1)
# print("Side 2:", triangle.side2)
# print("Hypotenuse:", triangle.hypotenuse)
# print("Perimeter:", triangle.perimeter())
# print("Circumscribed Circle Radius:", triangle.radius_of_circumscribed_circle())
# print("Angles:", triangle.angles())



