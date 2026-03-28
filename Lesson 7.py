'''I)
Напишите программу, которая, получает на вход целое положительное число с клавиатуры. Необходимо вывести все числа от 0 до N (N - Это введенное число), используя цикл while.'''

'''n = int(input("Enter a positive integer number: "))
i = 0

while n >= 0:
    print(i)
    i += 1
    n -= 1'''

'''II)
Напишите программу, которая получает на вход целое положительное число с клавиатуры. Необходимо, используя цикл while, вывести количество четных цифр в этом числе и их сумму.
'''
'''
n = int(input("Enter a positive integer number: "))
count = 0
sum = 0

while n > 0:
    if n % 2 == 0:
        sum = sum + n
        count = count + 1
    n -= 1

print(f"Sum of even numbers is {sum}")
print(f"Amount of even numbers is {count}")'''

#3
'''У пользователя запрашиваются два положительных числа X и R, причем X<R. Необходимо, используя цикл while, вывести на экран все числа из промежутка от X до R и посчитать их количество. При подсчете сами числа X и R включаются в данный промежуток и подсчитываются.
Пример:
вход:
2
4
Вывод:
2
3
4
В промежутке от X до R 3 числа
'''

x = int(input("Enter first positive number: "))
r = int(input("Enter second positive number bigger than first number: "))

if x < r:
    while x <= r:
        print(x)
        x += 1
else:
    print("The first number should be smaller than the second number, please try again.")