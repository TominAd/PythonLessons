import urllib
from urllib import request, parse
import sys

myUrl = "https://azbyka.ru/wp-content/uploads/2016/07/priroda.jpg"
myFile = "F:\\Python Lessons\\priroda.jpg"

try:

    print("Start Download file from" + myUrl)
    request.urlretrieve(myUrl, myFile)

except Exception:
    print("Erroe occuried during web request:!")
    print(sys.exc_info()[1])
    exit()
print("File download and saver :" + myFile)
