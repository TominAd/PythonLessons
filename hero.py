class Hero():
    """Class to Creat Hero"""
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all paramerts"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade level of Hero"""
        self.level += 1

    def move(self):
        """Start moving Hero"""
        print("Hero " + self.name + " start moving... ")

    def set_health(self, new_health):
        self.health = new_health
#__________________________________________________________________
#для любого изменения нужно деть свой dev свой метод


class SupperHero(Hero):
    """Class to Create Supper Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Supper Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100    #__self.__magic __ запрещает менять значение из вне класса

    def makemagic(self):
        """Use magik"""
        self.__magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(
            self.health) + " Magic is: " + str(self.__magic)).title()
        print(discription)