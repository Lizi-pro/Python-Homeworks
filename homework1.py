# 1. კონსოლიდან შეიტანეთ ორი რიცხვი და დაბეჭდეთ ყველა არითმეტიკული ოპერაცია
# (მიმატება, გამოკლება, გამრავლება, ჩვეულებრივი გაყოფა, მთელზე გაყოფა, ნაშთის აღება, ახარისხება).

# a = eval(input('Enter first number: '))
# b = eval(input('Enter second number: '))
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} ** {b} = {a ** b}')

# 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

# d1 = eval(input('Enter the size of first diagonal: '))
# d2 = eval(input('Enter the size of second diagonal: '))
# print(f'The ara of rhombus is {d1 * d2 / 2}')

# 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.

# a = eval(input('Enter number in meter: '))
# print(f'{a} meter = {a * 100} centimeters')
# print(f'{a} meter = {a * 10} decimeters')
# print(f'{a} meter = {a * 1000} millimeters')
# print(f'{a} meter = {a * 0.00062137} mile')

# 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა
# და ფუძის მნიშვნელობა.

# h = eval(input("Enter Height of Triangle: "))
# b = eval(input("Enter Base of Triangle: "))
# print(f'Area of Triangle is {h * b / 2}')

# 5. კონსოლიდან შეიტანეთ ორნიშნა რიცხვი და დაბეჭდეთ ციფრთა ჯამი.

# a = input('Enter number with two digits: ')
# print(int(a[0]) + int(a[1]))



# 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ
# შეტანილი რიცხვი არის თუ არა სიაში.

# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
# a = int(input('Enter a number: '))
# if a in num_list:
#     print('The number in list')
# else:
#     print('The number not in list')

# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას.
# თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

# a = int(input('Enter an integer: '))
# if a % 2 == 0:
#     print('the number is even')
# else:
#     print('The number is odd')

# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით,
# თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

# st1 = 'kantora'
# st2 = 'Kantora'
# if st1 is st2:
#     print('Same object')
# else:
#     print('Different object')

# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი
# "More than list elements"; თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.

# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
# a = int(input('Enter a number: '))
# if a > num_list[2] and a < num_list[-1]:
#     print('More than list elements')
# elif a == num_list[5]:
#     print('Equal')
# else:
#     print('None of the conditions were met')