# I) Используя лямбда-выражение и функцию filter создать программу, которая из введенной пользователем строки создает список, содержащий только цифровые символы. 
# user_string = input('Enter a srting: ')
# sorted_list = list(filter(lambda x: x.isdigit(), user_string))
# print(f'Строка пользователя: {user_string}')
# print(f'Список: {sorted_list}')

# II) Имеется список на 10 элементов, заполненный введенными пользователем числами. Необходимо на основе созданного списка создать новый список, в котором четные элементы первого списка умножены на 2, а нечетные на 3. Использовать функцию map() и лямбда-выражение. Вывести первоначальный список и получившийся список. Пример: первый список: [1, 2, 3, 4] получившийся список: [3, 4, 9, 8]
# print('You will need to enter 10 numbers.')
# user_list = []
# for i in range(1, 11):
#     while True:
#         try:
#             num = int(input(f'Enter a natural number {i}: '))
#             user_list.append(num)
#             break
#         except ValueError:
#             print('Error! Please enter the integer.')

# new_list = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, user_list))
# print(user_list)
# print(new_list)

# Задача №1: Конвертер цен.
# У тебя есть список цен в разных форматах (числа, строки, пустые значения):
# prices = [10, "25", 50, None, 100]
# Твоя цель:
# Используя map() и lambda, превратить этот список в рубли (курс 90).
# Программа должна:
# Умножать на 90 только то, что является числом.
# Корректно обрабатывать «мусор» (строки или None), чтобы код не падал.
# prices_list = [10, "25", 50, None, 100]
# num_list = [int(i) for i in prices_list if i is not None and str(i).isdigit()]
# ruble_list = list(map(lambda x: x * 90, num_list))
# print(f'Number list: {num_list}')
# print(f'Ruble list: {ruble_list}')

# Задача №2: Поиск длинных Title (Filter + Lambda)
# Попробуешь применить новые знания? Вот список:
# titles = ["SEO-блог", "Купить лучшие кроссовки в Москве с доставкой", "Контакты", 12345]
# Напиши фильтр, который оставит только заголовки длиннее 25 символов.
# Подсказка: не забудь про str(), так как в списке затесалось число 12345, которое может сломать len().
# titles = ["SEO-блог", "Купить лучшие кроссовки в Москве с доставкой", "Контакты", 12345]
# titles_len_over_25 = list(filter(lambda x: len(str(x)) > 25, titles))
# print(titles_len_over_25)

# Задача №3: Сортировка по расширению (sorted + lambda)
# Это последняя задача из блока Lambda-функций. Она чуть сложнее, потому что здесь lambda используется не для фильтрации или изменения, а как ключ для сортировки.
# Условие:
# Дан список файлов, которые ты выгрузил из папки проекта:
# files = ["script.js", "style.css", "index.html", "app.py", "main.py", "styles.css"]
# Твоя цель:
# Отсортировать этот список по расширению файла (то есть по буквам после точки), чтобы все .py были вместе, все .css вместе и так далее.

files = ["script.js", "style.css", "index.html", "app.py", "main.py", "styles.css", "Readme"]
files_sorted_list = list(sorted(files, key=lambda x: x.split('.')[-1]))
print(files_sorted_list)