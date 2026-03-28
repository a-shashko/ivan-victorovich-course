'''I)
Напишите программу, которая из введенной пользователем строки создаст список. Удалить из этого списка все буквы ‘a’, ‘e’, ‘u’. Строка вводится на английском и символы для удаления так же на английском языке.
'''
'''s = input("Enter a string: ")
l = list(s)
while l.count("a"):
    l.remove("a")
while l.count("e"):
    l.remove("e")
while l.count("u"):
    l.remove("u")
print(l)
'''
'''II)
Напишите программу, которая создаст список на 10 элементов, заполненный целыми числами, введенными с клавиатуры. Удалите все элементы, которые меньше 5 и найдите среднее арифметическое всех оставшихся элементов.
'''
'''print('You will need to enter 10 numbers')
my_list = []
for i in range(0, 10):
    num = int(input('Enter a number: '))
    my_list.append(num)
for i in range(0, 5):
    while i in my_list:
        my_list.remove(i)
avg = sum(my_list) / len(my_list)
print(avg)'''

'''III)
Напишите программу, которая создаст список на 10 элементов, заполненный целыми числами (положительными и отрицательными), введенными с клавиатуры. Отсортировать список в порядке убывания модулей чисел и вывести его на экран. Также найти произведение элементов кратных 3, имеющих четный индекс.
'''
print('You will need to enter 10 positive and negative integers')
my_list = []
m = 0
for i in range(0, 10):
    num = int(input('Enter a number: '))
    my_list.append(num)
my_list.sort(key=abs)
print(my_list)
for i in range(0, 10):
    if i % 2 == 0:
        for i in my_list:
            if i%3 == 0 and m == 0:
                m = m + i
            elif i%3 == 0 and m != 0:
                m = m * i
print(m)