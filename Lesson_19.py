def my_func():
    print("Внешняя функция")
    def my_inner_func():
        print('Вложенная функция')
    my_inner_func()
    print('Внешняя функция')

my_func()

# Задача 1: Создатель HTML-тегов
# В SEO часто приходится работать с разметкой. Напиши функцию tag_creator(tag), которая принимает название тега (например, "h1" или "p"). Внутри неё должна быть вложенная функция, которая принимает текст и возвращает его, обернутым в этот тег.
# def tag_creator(tag):
#     def wrapper(text):
#         return f"<{tag}>{text}</{tag}>"
#     return wrapper

# create_h1 = tag_creator("h1")
# print(create_h1)
# print(create_h1("Page Header"))

# Задача 2: Фабрика функций (Замыкание)
# Представь, что тебе нужно быстро создавать функции для разных математических операций. Напиши функцию power_factory(n), которая возвращает функцию, возводящую число в степень n.
# def power_factory(n):
#     def raise_number(base):
#         return base**n
#     return raise_number
# square = power_factory(2)
# print(square(5))

# Задача 3: Формировщик полных URL
# Часто при парсинге или аудите сайта мы имеем список относительных путей, которые нужно превратить в абсолютные ссылки. Напиши функцию url_generator(domain), которая принимает домен (например, https://example.com). Вложенная функция должна принимать путь страницы и возвращать полный корректный URL.
# Дополнительное условие: Вложенная функция должна проверять, не начинается ли путь со слеша /. Если начинается — склеивать аккуратно, чтобы не было двойного слеша (например, com//page).
# def url_generator(domain):
#     clear_domain = domain.rstrip("/")
#     def page_url(page):
#         return f"{domain}/{page.lstrip("/")}"
#     return page_url
# make_link = url_generator("https://mysite.com")
# print(make_link("contacts"))
# print(make_link("/blog"))