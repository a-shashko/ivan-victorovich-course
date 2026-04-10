# with open('example.txt', 'r', encoding='utf-8') as file:
#     srtings = [i.strip() + ' купить' for i in file.readlines()]

# print(srtings)
# with open('example.txt', 'r', encoding='utf-8') as file:
#     srtings = list(map(lambda x: x.strip() + ' купить', file.readlines()))

# print(srtings)

# Задание №1: "Чистильщик пустых строк"
# Часто при копировании ключевых слов из разных сервисов в файле появляются пустые строки или строки, состоящие только из пробелов. Они мешают скриптам.
# Условие:
#     Создай файл dirty_keywords.txt, где часть строк будут пустыми, а часть — с пробелами.
#     Напиши скрипт, который читает этот файл и создает новый файл clean_keywords.txt.
#     В новом файле не должно быть пустых строк.
# with open("input.txt", "r", encoding="utf-8") as file:
#     new_list = [i.strip() for i in file.readlines()]

# print(new_list)

# with open("output.txt", "w", encoding="utf-8") as file:
#     for i in new_list:
#         if i:
#             file.write(i + "\n")

# Задание №2: "Генератор URL"
# Теперь давай усложним задачу. Представь, что тебе нужно подготовить список URL для карты сайта (Sitemap).
# Условие:
#     Дан файл slugs.txt (создай его сам), где лежат названия разделов:
#     laptop
#     smartphone
#     headphones
#     Твой скрипт должен:
#         Прочитать этот файл.
#         Для каждой категории собрать полную ссылку вида https://mysite.com/catalog/название_категории/.
#         Записать всё это в файл urls_to_check.txt.
#         Важно: В самый верх итогового файла добавь строку-заголовок: --- Список URL для проверки ---.

# with open("input.txt", "r", encoding="utf-8") as file:
#     category_list = [i.strip() for i in file.readlines() if i.strip()]
#     print(category_list)

# with open("output.txt", "w", encoding="utf-8") as file:
#     file.write("--- Список URL для проверки ---" + "\n")
#     for i in category_list:
#         file.write(f"https://mysite.com/catalog/{i}/\n")

# Задание №3: "Анализатор логов" (Финал темы)
# Представь, что ты спарсил ответы сервера для списка страниц. У тебя есть файл log.txt с таким содержимым:
# https://site.com/main - 200
# https://site.com/about - 404
# https://site.com/contacts - 200
# https://site.com/services - 500
# https://site.com/blog - 404
# Твоя задача:
#     Прочитать этот файл.
#     Найти все строки, где статус не равен 200.
#     Записать только эти «проблемные» строки в новый файл errors.txt.

with open('input.txt', 'r', encoding='utf-8') as file:
    status_not_200 = [i.strip() for i in file.readlines() if '200' not in i]
    print(status_not_200)

with open('output.txt', 'w', encoding='utf-8') as file:
    for i in status_not_200:
        file.write(i + '\n')