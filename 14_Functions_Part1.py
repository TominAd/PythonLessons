
def napechatat_privetstvie(name):
    """Print privetstvie"""
    print("congratulations, " + name + " wish you all the best!!!!")
    print("Hello, Hello.")

def summa(x, y):
    print(x+y)

def summa1(x, y):
    s = x + y
    return s

print("___________________________")

napechatat_privetstvie("Tomin")
napechatat_privetstvie("Alan")
print("___________________________")

summa(10, 20)
x = summa1(120, 20)
print(x)
print("______________________________________")

def factorial(x):
    """Calculate Factorial"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet


print(factorial(1))
print(factorial(5))
print("_______________________")

for i in range(1, 10):
    print(str(i) + "! = " + str(factorial(i)))
