'''cycle = int(input("Enter the number of digits in the sequence of natural numbers: "))
sum = 0
for i in range(cycle):
    number = int(input("Enter number: "))
    if number % 6 == 0:
        sum += number
print(sum)'''
'''
I)
Напишите программу, вычисляющую сумму всех четных чисел от 0 до N (включительно).
N - целое число, введенное пользователем.
Для решения используйте цикл for.'''
'''
n = int(input("Enter a natural number: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)
'''
'''II)
Напишите программу, которая выводит числа от 1 до T, где T - это введенное пользователем целое число, которое больше или равно 35.
Если при выводе будут встречаться числа: 7, 13, 21, 29, то их нужно пропустить.
Для решения используйте цикл for, условную конструкцию if-elif-else и оператор continue.
'''
'''t = int(input("Enter a natural number >=35: "))
for i in range(1, t + 1):
    if i in {7, 13, 21, 29}:
        continue
    print(i)
    i += 1'''
'''III)
На вход поступает число N (пользователь вводит его с клавиатуры), используя цикл for необходимо организовать вывод от 1 до N (включительно).
Если число является четным, то выводим его квадрат (число в степени 2).
Если число нечетное, то выводим его куб (число в степени 3).
'''
n = int(input("Enter a natural number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        i **= 2
        print(i)
    else:
        i **= 3
        print(i)