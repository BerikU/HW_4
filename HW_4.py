# Вычислить число c заданной точностью d

# from decimal import Decimal
#
#
# def accuracy(num, acc):
#     number = Decimal(f'{num}')
#     return number.quantize(Decimal(f'{acc}'))

# print(accuracy(float(input('Enter a number: ')), float(input('Enter the accuracy: '))))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def find_prim_factors(num):
#     prim_fact = []
#     di = 2
#     while num > 1:
#         if num % di == 0:
#             prim_fact.append(di)
#             num /= di
#         else:
#             di += 1
#         return prim_fact
#
#
# print(find_prim_factors(int(input())))

# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности в том же порядке.

from random import randrange


def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums


def uniq_el(list_nums: list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)

    return result


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(uniq_el(all_list))