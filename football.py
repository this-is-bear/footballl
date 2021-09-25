class Football:
    def __init__ (self, name, position):
        self.name = name
        self.position = position

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я на позиции", self.position)

def main():
    crit1 = Football ("Лионель Месси", "нападающий")
    crit1.talk()
    crit2 = Football ("Неймар", "нападающий")
    crit2.talk()
    crit3 = Football ("Роберт Левандовский", "полузащитник")
    crit3.talk()
    crit4 = Football ("Кевин де Брюйне", "полузащитник")
    crit4.talk()
    crit5 = Football ("Мануэль Нойер", "защитник")
    crit5.talk()
    crit6 = Football ("Серхио Агуэро", "защитник")
    crit6.talk()
    crit7 = Football ("Артуро Видаль", "защитник")
    crit7.talk()
    crit8 = Football ("Джанлуиджи Буффон", "вратарь")
    crit8.talk()
    crit9 = Football ("Тьяго Алькантара", "нападающий")
    crit9.talk()
    crit10 = Football ("Матс Хуммельс", "полузащитник")
    crit10.talk()
    crit11 = Football ("Хамес Родригес", "вратарь")
    crit11.talk()
    print("Все мы играем за Буш Бакс")

main()