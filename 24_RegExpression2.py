import re

input_filname = "../Python Lessons/dumpfile.txt"
result_filename = "../Python Lessons/results.txt"

inputfile = open(input_filname, mode="r", encoding="Latin-1")
resultfile = open(result_filename, mode="w", encoding="Latin-1")
mytext = inputfile.read()

lookfor = r"[\w.~]+@(?!ntel\.com)"       # ?!и дальше пишем что хотим искличить из поиска

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")


print("Total: " + str(len(results)))