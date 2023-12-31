# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def  degree(a, b): #создаем функцию
    if b == 0:#если б равно нулю
        return 1#возвращается 1
    elif b < 0:#если отрицательное
        return 1 / degree(a, -b)
    elif b % 2 == 0:#если б четное 
        return degree(a * a, b // 2)
    else:
        return a * degree(a, b - 1)#если б нечетное

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
# вводим поочередно значения
result = degree(a, b)#переменная для вывода значения
print(f"{a} в степени {b} равно {result}")