# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).

# a = input('Enter some numbers: ')
# b = a.split()
# c = set(b)
# print(c)

# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე,
# რომლის შეცვლაც შეუძლებელი იქნება (frozenset).

# a = input('Enter some numbers: ')
# b = a.split()
# c = frozenset(b)
# print(c)

# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).

# a = {5, 10, 69, 56, 55, 86, 7, 6, 13}
# b = {136, 23, 89, 56, 4, 22, 47, 6}
# print(tuple(a) + tuple(b))

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple).
# დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).

# n = input('Enter numbers: ')
# t = tuple(int(c) for c in n.split())
# s = set(t)
# l = list(s)
# print(l)

# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# დაბეჭდეთ შემდეგი ფორმატით:
# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

# l = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# for t in l:
#     b = ''
#     c = ''
#     for a in t:
#         if type(a) == int:
#             b = a
#         else:
#             c = a
#     print(f'Name: {c}, Age: {b}')

# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# დავბეჭდოთ თანხვედრა.

# list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
# list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# intersection = set(list1).intersection(list2)
# print(list(intersection))