# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки.   Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.
from random import randint

# генерируем случайные числа X и Y
X = randint(1, 1000)
Y = randint(1, 1000)

# задаем подсказки
S = X + Y
P = X * Y

# выводим подсказки
print("Сумма чисел:", S)
print("Произведение чисел:", P)

# Катя должна отгадать числа X и Y
# для этого она может использовать формулы:
# X = (S +/- sqrt(S^2 - 4P)) / 2
# Y = (S +/- sqrt(S^2 - 4P)) / 2

# находим корни уравнения
D = S**2 - 4*P
if D < 0:
    print("Корней нет")
elif D == 0:
    X = Y = S / 2
    print("Ответ:", X, Y)
else:
    X1 = int((S + D**0.5) / 2)
    X2 = int((S - D**0.5) / 2)
    Y1 = int((S - D**0.5) / 2)
    Y2 = int((S + D**0.5) / 2)
    print("Ответ 1:", X1, Y1)
    print("Ответ 2:", X2, Y2)