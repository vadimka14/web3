# 1) Написать функцию, которая будет искать и выводить на экран минимальное число, большее 300 и кратное 19.

# def num(limit=300, dil=19):
#     while limit % dil != 0:
#         limit += 1
#     print(limit)
#
#
# num(341, 23)


#
# 2) Написать функцию, которая будет обменивать местами первую и последнюю цифру числа N (1234 → 4231).

# def swap(n):
#     return int(str(n)[3] + str(n)[1:3] + str(n)[0])
#
# print(swap(4351))

# def swap(n):
#     first = n // 1000
#     middle = n % 1000 // 10
#     last = n % 10
#     return int(str(last) + str(middle) + str(first))
#
# print(swap(1562))
#
# 3) Написать функцию, которая будет определять, делится ли число N на: 2, 3, 4, 5, ... (без использования оператора % )

# def withoutsp(current, number):
#     a = 0
#     while a < current:
#         a += number
#     if current == a:
#         print(f'{current} ділиться на {number}')
#     else:
#         print(f'{current}  не ділиться на {number}')
#
# withoutsp(20, 5)


#
# 4) Написать функцию, которая будет вычислять и выводить на экран значение выражения
# N^M без использования оператора возведения в степень (**).

# def multiple(number, times):
#     a = 1
#     for _ in range(times):
#         a *= number
#     return a
#
# print(multiple(19,3 ))
#
# 5) С клавиатуры вводится пять чисел. Для каждого из них вывести,
# является ли оно степенью числа 3. Вынести определение степени в функцию.

# def step(number, stepn=3):
#     a = 1
#     while a < number:
#         a *= stepn
#     if a == number:
#         print(f'{number} є степенем числа {stepn}')
#     else:
#         print(f'{number} не є степенем числа {stepn}')
#
# n = int(input())
# lst = [int(input()) for _ in range(n)]
#
# for l in lst:
#     step(l)


#
# 6) Реализовать набор функций для работы со списком:
# • Ввод с клавиатуры/инициализация случайными числами (с параметрами).
# import random
#
# def spysok(count):
#     numbers = [random.randint(1, 100) for _ in range(count)]
#     return numbers
#
# nums = spysok(10)

# • Вывод списка на экран (в одну строчку).

# def printer(nums):
#     print(*nums, sep=' ')
#
# printer(nums)

# • Подсчет максимума и минимума (с индексами).

# def maximum(nums):
#     print(f'Maximum {max(nums)} with index {nums.index(max(nums))}')
#
# maximum(nums)
#
# def minimum(nums):
#     print(f'Minimum {min(nums)} with index {nums.index(min(nums))}')
#
# minimum(nums)
#
#
# • Подсчет количества элементов, равных (больших/меньших) N.

# def equal(nums, n):
#     total = 0
#     for i in nums:
#         if i == n:
#             total += 1
#     print(f'Чисел, які дорівнюють {n} - {total}')
#
# equal(nums, 7)
#
#
# def more(nums, n):
#     total = 0
#     for i in nums:
#         if i > n:
#             total += 1
#     print(f'Чисел, які більші ніж {n} - {total}')
#
#
# more(nums, 10)
#
#
# def less(nums, n):
#     total = 0
#     for i in nums:
#         if i < n:
#             total += 1
#     print(f'Чисел, які менші ніж {n} - {total}')
#
#
# less(nums, 80)


# • Добавление элемента К [в конец массива/на N-ю позицию].

# def addition(nums, k, n):
#     new_lst = []
#     for i in range(len(nums)):
#         if i == n:
#             new_lst.append(k)
#         new_lst.append(nums[i])
#     if i == n - 1:
#         new_lst.append(k)
#     print(new_lst)
#
# addition(nums,420, 10)





# • Удаление из списка [последнего/Nго элемента].

# def deleted(nums, n):
#     del nums[n]
#     print(nums)
#
#
# deleted(nums, 4)


# • Сортировка списка по (возрастанию/убыванию). Повторяющиеся — убирать.

# gagsdg = [1, 3, 34, 3, 23, 1, 4, 3]
# def sortirovka(gagsdg):
#     new_nums = []
#     for i in gagsdg:
#         if not i in new_nums:
#             new_nums.append(i)
#     new_nums = sorted(set(gagsdg))
    # return sorted(new_nums)
#
#
# print(sortirovka(gagsdg))
#



#


# 7) Найти третий максимум в списке.

# lst = [int(input()) for _ in range(10)]
# def maximum(lst):
#     lst.remove(max(lst))
#     return lst
#
#
# lst = [2, 44, 56, 23, 12, 43, 65, 89, 908, 0, 54]
#
# for _ in range(2):
#     maximum(lst)
#
# print(max(lst))

# 8) Сдвинуть все элементы массива на два вправо. Оставшиеся элементы — поставить слева в том же порядке.
# lst = [2, 44, 56, 23, 12, 43, 65, 89, 908, 0, 54]
#
# new_lst = lst[-2:] + lst[:-2]
# print(new_lst)
#
# 9) Вставить K после максимального элемента.

# lst = [2, 44, 56, 23, 12, 43, 65, 89, 908, 0, 54]

# def appendix(lst, k):
#     maximum = max(lst)
#     new_lst = []
#     for i in lst:
#         new_lst.append(i)
#         if i == maximum:
#             new_lst.append(k)
#     return new_lst
#
#
# print(appendix(lst, 46))




appendix(lst, 10)