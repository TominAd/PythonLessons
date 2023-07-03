
name = input("Введите имя: ")
print("Privet " + name)

num1 = input("Vvedite X: ")
num2 = input("Vvedite Y: ")

summa = int(num1) + int(num2)
print(summa)

message = ""
while True:
    message = input("enter password:" + "  ")
    if message == '123':
        break
    print(message + "  " + "Password Not Correct")

print("Password was:" + "  " + message)

myList = []
msg =""
while msg != 'Stop'.upper():
    msg = input("Enter new item, and Stop to finish:")
    myList.append(msg)

print(myList)