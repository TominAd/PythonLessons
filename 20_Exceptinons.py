import sys

filename = "Lessons.txt"

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding='latin_1')
    except Exception:
        print("Inside EXPERT")
        print("Error Found")
        print(sys.exc_info()[1])
        # sys.exit() если бует ошибка чтоб преравть работу программы.
        filename = input("Enter correct file name! : ")
    else:
        print("Indise ELSE")
        print(myfile.read())
        sys.exit()

    finally:
       print("Inside FINALLY: ")

