# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list)
# და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# def zipi(*lists):
#     return list(zip(*lists))

# print(zipi(list1, list2))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.

# from functools import reduce

# params = [1, 2, 3, 4, 'sami']
# def multi(nums):
#     try:
#         return reduce(lambda a, b: a * b, nums)
#     except TypeError as ex:
#         return ex

# print(multi(params))

# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params = [1, 2, 3, 4, 5, 6, 7]

# def odds(nums):
#     return list(filter(lambda x: x % 2 != 0, nums))

# print(odds(params))

# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError),
# თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

# param1 = ['hello', 'world', 'coding', 'nod']
# param2 = 'ing'

# def func(words, word):
#     try:
#         return list(filter(lambda x: x.endswith(word), words))
#     except TypeError:
#         return 'TypeError'
#     except Exception as ex:
#         return ex

# print(func(param1, param2))






