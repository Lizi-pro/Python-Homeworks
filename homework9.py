import json
import os

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

chess_plus = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

file = 'chess_player.json'
with open(file, mode='w', encoding = 'utf-8') as f:
    json.dump(chess_players, f, indent=2)


# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის სახელს
# და დააბრუნებს ფაილის სრულ გზას.

# def filepath(file):
#     with open(file, mode='r') as f:
#         path = os.path.abspath(file)
#     return path

# print(filepath(file))

# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.

# def fileread(file):
#     with open(file, mode='r') as f:
#         read = f.read()
#     return read

# print(fileread(file))

# 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და დაამატებს ფაილის კონტენტს.

# def fileappend(file, new):
#     with open(file, mode='r', encoding='utf-8') as f:
#         data = json.load(f)
#         data.append(new)
#     with open(file, mode='w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2)
#     return 'DONE'

# for player in chess_plus:
#     print(fileappend(file, player))

# 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.

# def fileupdate(file, id, rating):
#     with open(file, mode='r', encoding='utf-8') as f:
#         data = json.load(f)
#     for player in data:
#         if player['id'] == id:
#             player['rating'] = rating
#             break
#     with open(file, mode='w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2)


