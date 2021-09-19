# # Пользователь вводит номер мобильного телефона
# # Программа провереяет введенный номер мобильного телефона
# # на правильность ввода, номер должен начинаться с +7 или 8 и
# # его вся длина(цифры и символы) должна быть равна либо 12 символов(1 случай) или  11 символов(2 случай).
#
# nomer = input('Ведите ваш номер мобильного телефона: ')
# mass1 = list(nomer)
# nomer_telefona = len(nomer)
# simvol = 12
# simvol_1 = 11
# if type(nomer_telefona) == int:   # Проверяем что введенные символы являются типом int
#     if nomer_telefona == simvol or simvol_1:   # Проверяем количество символов введенных символов
#         if mass1[0] == '+' and mass1[1] == '7':  # Проверяем с чего начинается номер
#             print('номер введен верно',nomer)
#         elif mass1[0] == '8':  # Проверяем с чего начинается номер
#             print('номер введен верно', nomer)
#         else:
#             print('номер введен не верно') # Говорит что номер введен не верно
# else:
#     print('номер введен не верно')


# Написать программу которая принимает от пользователя
# случайный набор символом и программа его находит (подбирает).
# import random
#
# chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# polzovatel = '4uQ8'
# dlina_polzovatela = len(polzovatel)
# popitok = 0
# while True:
#     for e in range(1):
#         password = ''
#         for i in range(dlina_polzovatela):
#             password += random.choice(chars)
#             if password == polzovatel:
#                 print('Пороль подобран верно', password, '==', polzovatel)
#                 popitok += 1
#                 print('Количество попыток:',popitok)
#
#             else:
#                 print('Пороль подобран неверно', password, '!=', polzovatel)
#                 popitok += 1
#                 print('Количество попыток:',popitok)
#     if password == polzovatel:
#         break


#Простой генератор сложных паролей
#
# import random
# chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# number = input('количество паролей?'+ "\n")
# length = input('длина пароля?'+ "\n")
# number = int(number)
# length = int(length)
# for n in range(number):
#     password =''
#     for i in range(length):
#         password += random.choice(chars)
#     print(password)

#Программа которая создает рандомную строку,
# потом ее удаляет и на ее месте создает новую и так бесконечно.
# import random
# import time
# chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# length = 10
# stroka = ''
# while length:
#     for i in range(random.randrange(5,50,5)):
#         stroka += random.choice(chars)
#     print(stroka, end='', flush=True)
#     time.sleep(0.1 )
#     print('\r', end='', flush=True)
#     stroka = ''

# Номера троллейбусных билетов представляют собой шестизначные
# числа. Счастливым считается тот билет, у которого сумма
# первых цифр равна сумме трех последних цифр. Например,
# билет 627 294 считается счастливым, так как
# 6 + 2 + 7 = 2 + 9 + 4=15. Найдите все номера счастливых
# билетов, такие, что из них можно извлечь натуральный корень
# какой-либо (превышающей 1)
# степени. Например, 720801‾‾‾‾‾‾‾√=849.
# Составьте программу для нахождения всех, номеров счастливых
# билетов, у которых сумма первых (последних) трех цифр,
# будучи возведенной в какую-либо степень, равна номеру
# счастливого билета.

# bilet = 627294
# mass = []
# h = 0
# s = 0
# f = 0
# w = " "
# mass1 = []
# for i in range(100000, 1000000):
#     mass.append(i)
#     h = ''.join(str(i))
#     h1 = h[:3]
#     h2 = h[3:]
#     #print(h1, h2)
#     for j in h1:
#         s += int(j)
#
#     for t in h2:
#         f += int(t)
#     if s == f:
#         print('Билет счастливый', h)
#     # else:
#     #     print('билет не счастливый', h)
#     s = 0
#     f = 0

#Заполнение двухмерного массива звездочками
import random
import numpy as np

def fifty(x,y):
    mass =[]
    for t in range(x):
        mass1 = []
        for g in range(y):
            d = random.choice('.')
            mass1.append(d)
        mass.append(mass1)
    return mass

Z = fifty(7,7)
Z = np.array(Z)
a = 0
b = 0
for i in range(len(Z)):  #0 1 2 3 4
    for j in range(len(Z[i])):  # 0 1 2 3 4
        Z[j][j] = '*'
        Z[j][-j-1] = '*'
        if j == b > 0:
            Z[a][b] = '*'
            Z[i][j] = '*'
            Z[j] = '*'
    a = i // 2
    b = j // 2
print(Z,a,b)