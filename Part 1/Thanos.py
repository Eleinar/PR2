class Rival:
    # Добавлен конструктор, чтобы иметь возможность выставлять количество жизней при создании
    def __init__(self, life):
        self.__life = int(life)

    # Метод attack переименован в take_damage и добавлена проверка на количество хп
    def take_damage(self):
        if self.__life > 0:
            print("Ouch!")
            self.__life -= 1

    # добавлен геттер для хп
    def get_life(self):
        return self.__life

    def checkLife(self):
        if self.__life <= 0:
            print("You won!")
        else:
            print(self.__life)

thanos = Rival(1000)
magneto = Rival(100)

for i in range(thanos.get_life()):
    thanos.take_damage()
thanos.checkLife()

for i in range(magneto.get_life()):
    magneto.take_damage()
magneto.checkLife()