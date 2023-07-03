from hero import *

myhero = Hero("Vurdalak", 4, "Orc")
mysuperhero = SupperHero("Moisey", 10, "Human", 5)

myhero.show_hero()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.magic = 10
mysuperhero.show_hero()
