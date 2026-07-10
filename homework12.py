# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y.
# კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი,
# რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, v):
#         new_x = self.x + v.x
#         new_y = self.y + v.y
#         return Vector(new_x, new_y)

#     def __str__(self):
#         return f'({self.x}, {self.y})'

# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v1)
# print(v2)
# print(v3)

# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი).
# კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __eq__(self, b):
#         return self.title == b.title and self.author == b.author

# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)
# print(book1 == book3)

# 3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და
# მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.
# Car კლასს დაუმატეთ  თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.
# დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის,
# მაგალითად year ატრიბუტი რომ იყოს ყოველთვის მთელი და ა.შ.

# import re
# from datetime import datetime

# class Car:
#     def __new__(cls, brand, model, year):
#         return super().__new__(cls)

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     @property
#     def brand(self):
#         return self._brand

#     @brand.setter
#     def brand(self, a):
#         if type(a) is not str or not re.fullmatch(r'[A-Za-z\s\-]+', a):
#             raise ValueError('Invalid Brand Name')
#         self._brand = a

#     @property
#     def model(self):
#         return self._model

#     @model.setter
#     def model(self, a):
#         if not re.fullmatch(r'[A-Za-z0-9\s\-]+', str(a)):
#             raise ValueError('Invalid Model Name')
#         self._model = a

#     @property
#     def year(self):
#         return self._year

#     @year.setter
#     def year(self, a):
#         if type(a) is not int or not 1886 <= a <= datetime.now().year:
#             raise TypeError('Invalid Year')
#         self._year = a


