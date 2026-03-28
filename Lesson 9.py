'''I)
Напишите программу, которая получает на вход строку и выводит:
1) Третий символ этой строки;
2) Первые 4 символа этой строки;
3) Все символы с четными индексами;
4) Все символы с нечетными индексами;
5) Все символы в обратном порядке.
'''
string = str(input("Enter a string: "))
print(string[2])
print(string[:4])
print(string[2::2])
print(string[1::2])
print(string[::-1])
'''II)
Напишите программу, которая получает на вход строку и делит ее на две равные части (если длина строки - четная, а если нечетная, то вторая часть должна быть на один символ больше).
'''
'''string = str(input("Enter a string: "))
length = len(string)
if length % 2 == 0:
    half = length // 2
    print(string[:half])
    print(string[half:])
else:
    half = (length + 1) // 2
    print(string[:half-1])
    print(string[half-1:])'''