

for x in range (0, 100 + 1, 2):         #цикл с условием от 0 до 100 и шаг 2 +1 чтоб 100 вошло в цикл
    print("Number x = " + str(x))   #Добавлдение написание в цикл коментариев
    if x == 10:                     #Преждевременная остановка цикла когда x = 10
        break                       #остановка цикла
print("END")
print("======================")

x = 0
while True:         #Бесканечный цикл
    x = x + 1       #Условие цикла
    print(x)        #вывод цикла
    if x == 10:     #остановка по выполнению условия
        break       #остановка цикла
print("END")