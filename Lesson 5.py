# Домашнее задание:
# I)
# Напишите программу, которая определяет наибольшее и наименьшее из двух чисел, введенных пользователем.
# II)
# Напишите программу, которая проверяет является ли введенное пользователем число четным.
# III)
# Напишите программу, которая, получает на вход 2 числа (большее и меньшее). Определить, кратно ли первое число второму. Вывести на экран сообщение об этом, а также остаток от деления, если первое число не кратно второму.

# 1
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("First number is greater than second number.")
elif x < y:
    print("First number is less than second number.")
else:
    print("First number is equal to second number.")'''

# 2
'''
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("First number is even")
else:
    print("First number is not even")'''

# 3
x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))

if x % y == 0:
    print("The first number is multiple of the second number")
else:
    c = x % y
    print(f"The first number is not multiple of the second number and remainder from division is equal to {c}")