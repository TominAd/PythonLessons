

meastring = "ну как то так"

name = "mr denis goroshko"




print(name.title())  # ставит заглавные буквы
print(name.upper())  # все заглавные буквы
print(name.lower())  # все маленькие буквы
print("stroka 1 \nstroka 2 \n\nstroka 3")   #перенос строки
print("stroka 1 \n\tstroka 2 \n\tтабуляция \n\tstroka 3 \nEND")   #табуляция строки


a = "         ...the end.......       "

print(a)
print(a.rstrip())   #стирает пробел вконце
print(a.lstrip())   #стирает пробел вначале
print(a.strip())    #стирает пробел везьде

b = a.strip(".")    #удаление точек
a = a.strip()       #удаление пробелов
print(a.title())

print("end")