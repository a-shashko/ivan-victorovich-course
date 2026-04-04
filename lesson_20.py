# Написать функцию, которая возвращает факториал введенного пользователем числа. Написать декоратор, который замеряет время выполнения данной функции. Не использовать модуль math. Для замера времени вам понадобится функция time() из модуля time.
# import time

# def timer_decorator(func):
#     def wrapper(n):
#         start_time = time.time()
#         result = func(n)
#         end_time = time.time()
#         timer = end_time - start_time
#         print(f'Time {timer}')
#         return result
#     return wrapper

# n = int(input('Enter a natural number: '))

# @timer_decorator
# def factorial(n):
#     fact = 1
#     for i in range(2, n + 1):
#         fact *= i
#     return fact

# print(f'Факториал равен: {factorial(n)}')

# Задача 1: Логирующий декоратор (Самая простая)
# Нужно написать декоратор debug, который просто сообщает: «Я начал работу над функцией такой-то». Это супер-полезно в SEO-скриптах, когда у тебя много этапов (парсинг, проверка ответов, запись в таблицу), и ты хочешь видеть в консоли, на каком этапе сейчас программа.
# def debug(func):
#     def wrapper():
#         print(f'[LOG]: Выполняю функцию {func.__name__}')
#         func()
#     return wrapper

# @debug
# def crawl_site():
#     print('Робот просматривает страницы ...')

# crawl_site()

# Задача 2 (Замыкания)
# Попробуй написать функцию-фильтр, про которую мы говорили раньше. Здесь декоратор не нужен, только вложенная функция.
# Задача: Напиши status_filter(target_code). Она должна возвращать функцию, которая принимает список кодов и оставляет только те, что равны target_code.
# def status_filter(target_code):
#     def filter_logic(codes_list):
#         filtered_list = [i for i in codes_list if i == target_code]
#         return filtered_list
#     return filter_logic

# only_404 = status_filter(404)
# print(only_404([404, 500, 301, 200, 404]))


# Задача 3: Декоратор "Admin"
# У тебя есть функция, которая удаляет битые ссылки из базы. Это опасная операция. Тебе нужен декоратор, который проверяет: является ли пользователь админом.
def admin_required(func):
    def wrapper(*args, **kwargs):
        if "admin":
            return func()
        else:
            print("Access denied!")

    return wrapper


@admin_required
def delete_links(a):
    print("Все битые ссылки удалены из базы!")


delete_links("admin")
