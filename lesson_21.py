# I) Используя лямбда-выражение и функцию filter создать программу, которая из введенной пользователем строки создает список, содержащий только цифровые символы. 
# user_string = input('Enter a srting: ')
# sorted_list = list(filter(lambda x: x.isdigit(), user_string))
# print(f'Строка пользователя: {user_string}')
# print(f'Список: {sorted_list}')

# II) Имеется список на 10 элементов, заполненный введенными пользователем числами. Необходимо на основе созданного списка создать новый список, в котором четные элементы первого списка умножены на 2, а нечетные на 3. Использовать функцию map() и лямбда-выражение. Вывести первоначальный список и получившийся список. Пример: первый список: [1, 2, 3, 4] получившийся список: [3, 4, 9, 8]
print('You will need to enter 10 numbers.')
user_list = []
for i in range(1, 11):
    while True:
        try:
            num = int(input(f'Enter a natural number {i}: '))
            user_list.append(num)
            break
        except ValueError:
            print('Error! Please enter the integer.')

new_list = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, user_list))
print(user_list)
print(new_list)
