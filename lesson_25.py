# # import this
# import math
# print(dir(math))
# # print(help(math))
# Задача: «SEO-таймер и логирование»
# Тебе нужно написать программу, которая имитирует начало работы парсера.
# Условие:
#     Подключи модули os и datetime.
#     Получи текущую дату и время.
#     Создай строку с датой в формате: ДЕНЬ_МЕСЯЦ_ГОД (например, 11_04_2026).
#     Используя модуль os, проверь, существует ли папка с таким названием:
#         Если нет — создай её.
#         Если да — ничего делать не нужно (чтобы не было ошибки).
#     Внутри этой папки создай файл run_log.txt.
#     Запиши в этот файл строку с точным временем запуска в формате: [ЧАСЫ:МИНУТЫ:СЕКУНДЫ] Сессия запущена.
#     Важно: Открывай файл в режиме дозаписи ('a'), чтобы при каждом запуске скрипта в файл добавлялась новая строка, а не стиралась старая.
# import os
# import datetime
# now = datetime.datetime.now()
# formated_date = now.strftime('%d_%m_%Y')
# formated_time = now.strftime('%H:%M:%S')
# if not os.path.exists(formated_date):
#     os.makedirs(formated_date)
# file_path = os.path.join(formated_date, 'run_log.txt')
# with open(file_path, 'a', encoding='utf-8') as file:
#     file.write(f'[{formated_time}] Сессия запущена\n')

