
import json
filename = "../Python Lessons/user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')
player1 = {
    'PlayerName': "Donald Tramp",
    'Score': 345,
    'Awards': ["QR", "NV", "NY"]

}

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'Awards': ["WT", "TX", "MI"]

}

player3 = {
    'PlayerName': "Tomin Tollan",
    'Score': 347,
    'Awards': ["WT", "TX", "MI"]

}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)
myplayers.append(player3)

#================save by end===============


json.dump(myplayers, myfile) #сохрение в файл
myfile.close() # закрыть файл

#-----------load by json--------
myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("player Name is: " + str(user["PlayerName"]))
    print("player Score is: " + str(user["Score"]))
    print("player Awards №1: " + str(user["Awards"][0]))
    print("player Awards №2: " + str(user["Awards"][1]))
    print("player Awards №3: " + str(user["Awards"][2]))
    print("===================================\n")