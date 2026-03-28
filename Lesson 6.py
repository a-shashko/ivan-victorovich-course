'''
Домашнее задание:
I)
Напишите программу, которая, получает на вход три числа. Выведите сумму наибольшего и наименьшего из трёх чисел.
II)
Напишите программу, определяющую является ли введённый пользователем год високосным.
III)
Напишите программу, которая запрашивает у пользователя месяц его рождения в формате от 1 до 12.
Необходимо определить и вывести время года.
Формат вывода (пользователь должен увидеть):
Вы родились осенью
или
Вы родились летом
или
Вы родились зимой
или
Вы родились весной
Для решения задания используйте конструкцию match/case.'''

# 1
'''
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x > y > z or x < y < z:
    print(f"Summ of the biggest and the smallest number is {x + z}")
elif y > z > x or y < z < x:
    print(f"Summ of the biggest and the smallest number is {x + y}")
elif z > x > y or z < x < y:
    print(f"Summ of the biggest and the smallest number is {z + y}")'''

# 2
'''
year = int(input("Enter the year: "))

if year % 400 == 0:
    print("The year is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")'''

# 3
month = int(input("Enter your birthday month: "))

match month:
    case 12 | 1 | 2:
        print("Вы родились зимой.")
    case 3 | 4 | 5:
        print("You were born in spring.")
    case 6 | 7 | 8:
        print("You were born in summer.")
    case 9 | 10 | 11:
        print("You were born in autumn.")
    case _:
        print("Wrong input.")