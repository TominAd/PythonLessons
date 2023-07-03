inputfile = "../Python Lessons/user_names.txt"
"""Чтение с файла с вывод на экран только фамилии Давидсон"""
myfile = open(inputfile, mode='r', encoding='latin_1')

for num, line in enumerate(myfile, 1):
    if "Davidson" in line:
        print("Line №: " + str(num) + " : " + line.strip())

print("_________________________________________")

inputfile = "../Python Lessons/list_of_password.txt"


myfile1 = open(inputfile, mode='r', encoding='latin_1')
"""Чтение с файла и поск всех паролей в котором есть 12345678"""
for num, line in enumerate(myfile1, 1):
    if "123456789" in line:
        print("Line №: " + str(num) + " : " + line.strip())
print("_________________________________________")


outputfile = "../Python Lessons/my_passwords.txt"
password_tolookfor = "123456"
"""Чтение и запись и поиск паролей vasya в файл"""
myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='w', encoding='latin_1') # mode='w' обнуляет файл
for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line №: " + str(num) + " : " + line.strip())
        myfile2.write("Found Passwors: " + line)
print("_________________________________________")

outputfile = "../Python Lessons/my_passwords.txt"
password_tolookfor = "samsung"
"""Чтение и запись и поиск паролей samsung в файл"""
myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')  # mode='a' добавляет в файл
for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line №: " + str(num) + " : " + line.strip())
        myfile2.write("Found Passwors: " + line)
print("_________________________________________")

outputfile = "../Python Lessons/my_passwords.txt"
password_tolookfor = "killer"
"""Чтение и запись и поиск паролей killer в файл"""
myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')  # mode='a' добавляет в файл
for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line №: " + str(num) + " : " + line.strip())
        myfile2.write("Found Passwors: " + line)
print("_________________________________________")

myfile.close()
myfile1.close()
myfile2.close()