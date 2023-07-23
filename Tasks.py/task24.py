#  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


N = int(input("Введите количество кустов на грядке: "))
berries = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))
#запрашиваем сколько кустов на грядке
#функция мап применяет заданную функцию к каждому обьекту
#сплит разделяет строку на подстроки

max_berries = 0 #создаем пременную со значением 0
for i in range(N):#проходим по каждому элемента списка 
    curr_berries = berries[i] + berries[(i-1)%N] + berries[(i+1)%N]#суммируем количество ягод на текущем,предыдущем,следующем кусте.
    #%N зацикливаетсписок кустов
    if curr_berries > max_berries:#сравниваем текущее количество ягод с максимальным количеством ягод,
       max_berries = curr_berries  #если оно больше обновляем значение переменной макс ягоды
     

print("Максимальное количество ягод, которое может собрать собирающий модуль за один заход:", max_berries)