"""
8. (МОДУЛЬ 3) В проекте создать новый модуль bornday.py
9. Написать программу или модернизировать предыдущую используя условные операторы:
- Спросить у пользователя год рождения А.С. Пушкина
- Если пользователь ввел верный год спросить у него день рождения
- Если день рождения введен верно вывести 'Верно'
- Если день рождения введен неверно вывести 'Неверный день рождения'
- Если неверно введен год, то сразу вывести 'Неверный год рождения', а день рождения не спрашивать
"""

# Подключаем метод модуля для проверки ответа на число
from functions import check_ans_num

print('Добрый день')
question_1 = 'В каком году родился А.С.Пушкин?'
question_2 = 'Введите месяц рождения А.С. Пушкина'
question_3 = 'Введите день'

# Пустые ответы
answer_1 = ''
answer_2 = ''
answer_3 = ''

print('Ответьте на несколько вопросов: ')
answer_1 = check_ans_num(question_1)
if answer_1 == 1799 or answer_1 == 99:
    answer_2 = int(check_ans_num(question_2))
    if answer_2 == 6:
        answer_3 = int(check_ans_num(question_3))
        if answer_3 == 6:
            print('Верно')
        else:
            print('Неверный год')
else:
    print('Не верно')