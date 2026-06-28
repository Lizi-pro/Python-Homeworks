# შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0

import os, csv
headers = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']

students = [
  {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
  {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
  {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
  {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
  {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
  {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
  {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]

with open('students.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(students)

# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი სტუდენტს დაამატებს csv ფაილში.
#    დაასორტირეთ მონაცემები id-ის მიხედვით.

# def addstudent():
#     newdata = []
#     with open('students.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for i in reader:
#             i['id'] =  int(i['id'])
#             newdata.append(i)

#     print('Input new students data')
#     id = int(input('ID: '))
#     name = input('Name: ')
#     age = input('Age: ')
#     grade = input('Grade: ')
#     subject = input('Subject: ')
#     mark = input('Mark: ')

#     new_student = {'id': id, 'name': name, 'age': age, 'grade': grade, 'subject_name': subject, 'mark': mark}

#     newdata.append(new_student)

#     sortdata = sorted(newdata, key=lambda x: x['id'])

#     with open('students.csv', mode='w', encoding='utf-8', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(sortdata)

#     print('Student Added')

# addstudent()

# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა,
#    ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.

# def readdata():
#     a = input('If you want to read all students info write "all" or write student id: ')
#     with open('students.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         if a == 'all':
#             for i in reader:
#                 print(i)
#         else:
#             for i in reader:
#                 if i['id'] == a:
#                     print(i)
#                     break

# readdata()

# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.

# def avmark():
#     subjects = []
#     studentsdata = []
#     with open('students.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for i in reader:
#             studentsdata.append(i)

#             subject = i['subject_name']
#             if subject not in subjects:
#                 subjects.append(subject)

#         for subject in subjects:
#             marks = 0
#             count = 0
#             for i in studentsdata:
#                 if i['subject_name'] == subject:
#                     marks += int(i['mark'])
#                     count += 1
#             av = marks/count
#             print(subject, av)

# avmark()

# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება
#    სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის `id`,
#    საგანს და განახლებულ ქულას.

# def changemark():
#     a = input('Wrire the id of student: ')
#     b = input('Write subject: ')
#     c = input('Write students new mark: ')
#     studentsdata = []
#     with open('students.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for i in reader:
#             studentsdata.append(i)

#         for i in studentsdata:
#             if i['id'] == a:
#                 if i['subject_name'] == b:
#                     i['mark'] = c
#     with open('students.csv', mode='w', encoding='utf-8', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(studentsdata)

# changemark()

# 5. დაამატეთ ახალი სტუდენტი და ჩაწერეთ ფაილში.

new_student = {
  'id': 5,
  'name': 'Demetre',
  'age': 18,
  'grade': 'A',
  'subject_name': 'Informatic',
  'mark': 94
}

# new = []
# with open('students.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for i in reader:
#         new.append(i)
#     new.append(new_student)
# with open('students.csv', mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(new)



