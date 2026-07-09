# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით მეთოდი car_info(),
# რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def car_info(self):
#         print(self.brand, self.model, self.year)

# honda = Car('Honda', 'Fit', 2016)
# honda.car_info()

# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.
# ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def age_of_car(self):
#         age = 2026 - self.year
#         return age

#     def car_info(self):
#         car_age = self.age_of_car()
#         print(self.brand, self.model, self.year, car_age)

# honda = Car('Honda', 'Fit', 2016)
# honda.car_info()

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს.
# დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(),
# რომელიც დაბეჭდავს შემდეგ სტრიქონს "ელემენტის ხანგრძლივობა შეადგენს [battery_life] საათს".

# class ElectricCar(Car):
#     def __init__(self, brand, model, year, battery_life):
#         super().__init__(brand, model, year)
#         self.battery_life = battery_life

#     def battery_info(self):
#         print(f'ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს')

# electro = ElectricCar('Kia', 'EV6', 2024, 6)
# electro.car_info()
# electro.battery_info()

# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას.
# გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას.

# class Car:
#     number_of_cars = 0
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#         Car.number_of_cars += 1

#     def age_of_car(self):
#         age = 2026 - self.year
#         return age

#     def car_info(self):
#         car_age = self.age_of_car()
#         print(self.brand, self.model, self.year, car_age)


# honda = Car('Honda', 'Fit', 2016)
# honda.car_info()

# 5. Car კლასს დაამატეთ კლასის მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

# class Car:
#     number_of_cars = 0
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#         Car.number_of_cars += 1

#     def age_of_car(self):
#         age = 2026 - self.year
#         return age

#     def car_info(self):
#         car_age = self.age_of_car()
#         print(self.brand, self.model, self.year, car_age)

#     @classmethod
#     def total_cars(cls):
#         print(cls.number_of_cars)

# carnum = Car.total_cars()

