"""def fun1(a, b):
    return a * b
result = fun1(5, 10)
print(result)"""

# I) Написать функцию, которая в качестве аргумента получает радиус круга. Радиус вводится пользователем с клавиатуры. Функция считает площадь круга. Формула площади круга: S = pi * R^2, где pi - константа 3.14, R - радиус. Функция возвращает значение площади.
"""pi = 3.14
def fun1(R):
    return pi * R**2
R = int(input('Enter radius: '))
S = fun1(R)
print(S)"""


# II) Написать функцию, которая в качестве аргумента принимает целое число, введенное пользователем. Функция возвращает количество четных цифр в числе и их сумму.
def fun1(a):
    count1 = 0
    sum1 = 0
    for i in list(a):
        i = int(i)
        if i % 2 == 0:
            count1 += 1
            sum1 = sum1 + i
    return count1, sum1


a = input("Enter a number: ")
count1, sum1 = fun1(a)
print(count1)
print(sum1)
