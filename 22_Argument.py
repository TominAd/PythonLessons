import sys
import os
#print("Hello World")
#print(sys.argv[1:])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help")
        print("Usage of this")
    print("Argument enter: " + str(sys.argv[1:]))
else:
    print("Argument not Provided")

os.system("dir > test.txt")
os.mkdir("my dir")
sys.exit(2)