import urllib
from urllib import request

myUrl = "https://astahov.net"
myUrl1 = "https://google.com"


otvet = request.urlopen(myUrl)
mytext1 = otvet.readlines()
mytext2 = otvet.read()

otvet1 = request.urlopen(myUrl1)
mytext3 = otvet.readlines()
mytext4 = otvet.read()


print(otvet)
print(mytext2)

for line in mytext1:
    print(line)

print(otvet1)
print(mytext4)

for line in mytext3:
    print(line)