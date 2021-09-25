class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, 
              ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            self.__pass_time()

    def play(self, fun = 4):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Поиграть со зверюшкой 5 минут
        3 - Поиграть со зверюшкой 10 минут
        4 - Поиграть со зверюшкой 15 минут
        5 - Поиграть со зверюшкой больше 20 минут
        6 - Покормить зверюшку (дать 100 г корма)
        7 - Покормить зверюшку (дать 150 г корма)
        8 - Покормить зверюшку (дать 200 г корма)
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")
        if choice == "2":
            print("Я не наигрался!")
            crit.play()
        if choice == "3":
            print("Было весело,но маловато")
            crit.play()
        if choice == "4":
            print("Уииииии!")
            crit.play()
        if choice == "5":
            print("Фух,я устал(а)")
            crit.play()
        if choice == "6":
            print("Ну,можно было и больше")
            crit.eat()
        if choice == "7":
            print("Ммм,спасибо")
            crit.eat()
        if choice == "8":
            print("Мммммм,я слишком много съел(а)")
            crit.eat()
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        
        elif choice == "2":
            crit.play()

        elif choice == "3":
            crit.play()
        
        elif choice == "4":
            crit.play()
         
        elif choice == "5":
            crit.play()
    
        elif choice == "6":
            crit.eat()

        elif choice == "7":
            crit.eat()

        elif choice == "8":
            crit.eat()

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()
