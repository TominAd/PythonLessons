import pypyodbc

mySQLServer = "Manowar\SQLEXPRES"
myDataBase = "northwind"

connection = pypyodbc.connect('Driver=(SQL Server);'
                              'Server='+ mySQLServer + ';'
                              'Database=' + myDataBase + ';')

# такой вариант если сразу прописать кто будет пожключаться к базе
#connection = pypyodbc.connect('Driver=(SQL Server);'
#                              'Server=Manowar\SQLEXPRES;'
#                             'Database=northwind;'
#                              'uid=username;'
#                             'pwd=pmpasword;')

cursor = connection.cursor()
#Запрос в базу данных что именно и с какй таблицы выгребать, выбираем с базы все
mySQLQuery = ("""
                SELECT CompanyName, CantactName, Country
                FROM dbo.Customers
                WHERE country = 'Canada'
              """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    CompanyName = row[0]
    CantactName = row[1]
    Country = row[2]

    print("Welcom : " +str(CompanyName) + "User :" + str(CantactName) + " From :" + str(Country))

connection.close()

