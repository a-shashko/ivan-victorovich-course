'''I)
Напишите программу, которая получает на вход строку и символ. Определите сколько раз в введенной строке встречается введенный символ.
Пользователь вводит строку, необходимо посчитать сколько в этой строке встречается букв "y" и "s" (в обоих регистрах). Ввод и проверки осуществляются на английском языке.
Вывод должен иметь вид:

Буква &#039;y&#039; встречается XXXX раз
Буква &#039;s&#039; встречается XXXX раз
Если нет таких букв то:
В введенном предложении нет букв &#039;y&#039; и &#039;s&#039;.
'''
'''s = input("Enter a string: ")
symbol = input("Enter a symbol: ")
print(s.count(symbol))'''
'''s = input("Enter a string: ").lower()
quantityY = s.count("y")
quantityS = s.count("s")
if quantityY != 0 | quantityS != 0:
    print("Letter \"y\" occurs ", quantityY, " times.")
    print("Letter \"s\" occurs ", quantityS, " times.")
else:
    print("There is no letter \"y\" or \"s\" in the string.")'''

'''II)
Напишите программу, которая получает на вход строку. В введенной строке измените регистр букв на противоположный и удалите все пробелы.'''
s = input("Enter a string: ").swapcase()
print(s.replace(" ", ""))