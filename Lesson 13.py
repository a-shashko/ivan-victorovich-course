'''I) Напишите программу, которая создает кортеж на 15 элементов, заполненный квадратами целых чисел от 1 до 15. В качестве результата работы выведите все элементы кортежа в порядке убывания. '''
'''y = tuple(sorted((i**2 for i in range(1, 16)), reverse = True))
print(y)'''

'''II) Имеется кортеж списков: letters = (['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']) Напишите программу, которая добавляет символ '!' в начало каждого списка. '''
'''letters = (['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'])
for letter in letters:
    letter.insert(0, '!')
print(letters)
'''
'''count = len(letters)
for i in range(0, count):
    letters[i].insert(0, '!')
print(letters)'''

'''III) Напишите программу, которая создает кортеж из 10 элементов, заполненный натуральными числами, введенными с клавиатуры. На его основе создайте кортеж, в котором будут сначала все элементы, отсортированные в порядке убывания чисел, а затем - в порядке возрастания. Полученный кортеж (в нем должно быть 20 элементов) выведите на экран.'''
print("You will need to enter 10 natural numbers.")
int_tuple = tuple()
for i in range(0, 10):
    string = input(f"{i}. Enter natural numbers: ")
    int_tuple = tuple((map(int, string))) + int_tuple
tuple_des = tuple(sorted(int_tuple, reverse = True))
tuple_asc = tuple(sorted(int_tuple))
tuple_merge = tuple_des + tuple_asc
print(tuple_merge)
