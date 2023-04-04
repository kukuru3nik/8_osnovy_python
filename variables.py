"""
1. Создать новый проект
2. (МОДУЛЬ 1) В проекте создать новый модуль variables.py
3. Выбрать объект для описания из списка: овощ, еда, сотрудник, игрушка (так же можно придумать свой)
4. Объявить переменные основных типов данных для описания этого объекта:

Например объект школьник:
имя (тип строка), возраст (тип целое число), класс (тип целое число), отличник или нет (логический тип), средняя оценка (число с плавающей точкой)

Чем больше переменных (характеристик), тем лучше. Минимально 4 переменные для типов (строка, число, число с плавающей точкой, логический тип)

5. В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных
"""

# Объект для описания: Пшеница
# Характеристика родов зерновых культур по соцветиям и зерну

name = 'Пшеница'
latin_name = 'Triticum'
type_inflorescence = 'колос'
spikelets_num = 1
min_flowers_num = 3
max_flowers_num = 5
spikelet_scales = 'широкие'
outer_flower_scales = 'гладкие'
grain_shape = 'продолговато-овальная'
grain_ilminess = 'обычное голое'
shape_groove = 'широкая'
presence_tuft = True
grain_surface = 'гладкая'
grain_coloring = 'белая'

sings_list = [name, latin_name, type_inflorescence, spikelets_num, min_flowers_num, max_flowers_num, spikelet_scales,
              outer_flower_scales, grain_shape, grain_ilminess, shape_groove, presence_tuft, grain_surface,
              grain_coloring]
sing_num = len(sings_list)


# Выводим типы на экран
for i in range(sing_num):
    print(type(sings_list[i]))
