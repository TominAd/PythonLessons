


#         0      1      2       3         4

cars = ['bmv', 'vw', 'lada', 'seat', 'shkoda']

for x in cars:              #печать всего масива через Х используя цикл
    print(x.upper())

for x in range(1, 6):
    print(x)

mynumber_list = list(range(10, 10 + 1, 2))
print(mynumber_list)
print("===========================")


for x in mynumber_list:
    x = x * 2
    print("what is:" + str(x))

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number:" + " " + str(max(mynumber_list)))
print("===========================")
print("Min number:" + " " + str(min(mynumber_list)))
print("===========================")
print("Sum:" + " " + str(sum(mynumber_list)))
print("===========================")

#         0      1      2       3         4
cars = ['bmv', 'vw', 'lada', 'seat', 'shkoda']

mycars = cars[1:4]
print(mycars)

print("===========================")
mycars = cars[:4]
print(mycars)
print("===========================")

mycars = cars[-3:-1]
print(mycars)
print("===========================")

#         0      1      2       3         4
cars = ['bmv', 'vw', 'lada', 'seat', 'shkoda']
mycars = cars[:]
mycars.sort(reverse=True)
print(mycars)
print(cars)