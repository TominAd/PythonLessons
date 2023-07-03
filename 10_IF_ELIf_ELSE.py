
x = 25

if x == 24:
    print("YES ")
else:
    print("no you")

age = 30
if age <=4:
    print("You are baybi")
elif (age > 4) and (age < 12):
    print("You are kids")
elif (age >= 12) and (age <19):
    print("You are  teneger")
else:
    print("Ты старпер")
print("=====END=====")

all_cars = ['crusler', 'dacia', 'bmv', 'KIA', 'vw', 'seat', 'shkoda', 'lada', 'audi', 'ford', 'Chevrolet']
german_cars = ['bmv', 'vw', 'audi']
if 'lada' in all_cars:
    print("YES LADA")
else:
    print("no")

all_cars = ['crusler', 'dacia', 'bmv', 'KIA', 'vw', 'seat', 'shkoda', 'lada', 'audi', 'ford', 'Chevrolet']
german_cars = ['bmv', 'vw', 'audi']

for xxxx in all_cars:
   if xxxx in german_cars:
       print(xxxx + " German car")          #сравниваем два масива и выводим все значения
   #else:
    #  print(xxxx + " no german car")       #если не надо то убиравем это условие и будет печатать только правильный список