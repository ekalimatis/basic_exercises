from collections import defaultdict


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_count = defaultdict(int)
for student in students:
    names_count[student['first_name']] += 1
for name, count in names_count.items():
    print(f'{name}: {count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names_count = defaultdict(int)
for student in students:
    names_count[student['first_name']] += 1
max_name = max(names_count, key=names_count.get)
print(f'Самое частое имя среди учеников: {max_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for n, clas in enumerate(school_students, 1):
    names_count = defaultdict(int)
    for student in clas:
        names_count[student['first_name']] += 1
    most_frequent_name = max(names_count, key=names_count.get)
    print(f'Самое частое имя в классе {n}: {most_frequent_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for clas in school:
    male = 0
    female = 0
    for student in clas['students']:
        if is_male[student['first_name']]:
            male += 1
        else:
            female += 1
    print(f"Класс {clas['class']}: девочки {female}, мальчики {male}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_male_clas = {}
max_female_clas = {}
for clas in school:
    male = 0
    female = 0
    for student in clas['students']:
        if is_male[student['first_name']]:
            male += 1
        else:
            female += 1
    if male > max_male_clas.get('count', 0):
        max_male_clas = {'class': clas['class'], 'count': male}
    if female > max_female_clas.get('count', 0):
        max_female_clas = {'class': clas['class'], 'count': female}
print(f"Больше всего мальчиков в классе {max_male_clas['class']}")
print(f"Больше всего мальчиков в классе {max_female_clas['class']}")
