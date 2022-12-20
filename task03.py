# Задача 3
# Реализуйте алгоритм перемешивания списка.

from random import randint
first_list = [10, 20, 30, 40, 50]
print('Изначальный список: ')
print(first_list)
mixed_list = first_list[:]
for i in range(len(mixed_list)):
    random_num = randint(i, len(mixed_list)-1)
    temp = mixed_list[i]
    mixed_list[i] = mixed_list[random_num]
    mixed_list[random_num] = temp

print('Перемешанный список: ')
print(mixed_list)