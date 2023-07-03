


cities = ['New York', 'Moscow', 'new delly', 'simferopol', 'toronto'] #объявлдение массива

print(cities)
print(len(cities))              #колличество записей в масиве



print(cities[-2].upper())           #показать указанный номер массива, все большие буквы
print(cities[2].title())            #показать указанный номер массива, первые буквы заглавные
print(cities[2].upper())            #показать указанный номер массива, все большие буквы

cities[2] = 'Tula'                  #замена в массиве в указанном месте массива
print(cities)

cities.append('Kharkov')            #добавление в массив в конец
cities.append('Kiev')               #добавление в массив в конец
print(cities)

cities.insert(2, 'Pervomayskiy')    #добавление в массив в указанное место
print(cities)

del cities[-1]                      #удаление с масива
print(cities)

cities.remove('Tula')               #при указании имени объекта для удаления регистр имеет значение
print(cities)

deleted_cite = cities.pop(2)         #стирает послений массив либо указываем какую часть удалить
print("delele cities:" + " " + deleted_cite)
print(cities)


cities.sort()                       #сортировка по алфавиту
print(cities)


cities.sort(reverse=True)                       #сортировка по  алфовиту в обратную сторону
print(cities)

cities.reverse()
print(cities)