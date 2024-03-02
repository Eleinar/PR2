class SoyuzDocking:
    def __init__(self):
        self.distance = 500
        self.speed = 50
        self.fuel = 100

    def perform_burn(self, burn_amount):
        self.speed = max(self.speed - burn_amount, 0)
        self.fuel = max(self.speed - burn_amount, 0)

    def update_distance(self):
        self.distance = max(self.distance - self.speed, 0)

    def has_docked(self):
        return self.distance <= 0

def main():
    print("Добро пожаловать в симуляцию стыковки Союз Т-6!.")
    print("Ваша миссия - стоковка со станцией Салют-7.")
    print("Вы можете управлять скоростью косиического корабля сжигая, топливо")
    print("Кадлая еденица сожжённого топлива замедляет космический корабль на 1 м/с")
    print("Удачи экипажу!\n")

    docking_sequence = SoyuzDocking()
    # Главный игровой цикл
    while not docking_sequence.has_docked():
        print(f"Расстояние до Салют-7: {docking_sequence.distance} метров")
        print(f"Скорость: {docking_sequence.speed} м/с")
        print(f"Топливо: {docking_sequence.fuel} кг")
        # Проверка на отсутствие топлива. Если нет, то миссия провалена
        if docking_sequence.fuel <= 0:
            print("Топливо кончилось! Состыковка не удалась!")
            break
        # Проверка на дистанцию. Если < 11, то предлагается включить автопилот
        if docking_sequence.distance < 11:
            autopilot = input("До станции Салют-7 осталось менее 11 метров.\nАктивировать режим автопилота для автоматической состыковки? (да/нет): ")
            if autopilot.lower() == 'да':
                print("Автопилот активирован")
                break

        # Предложение игроку сжечь топливо для снижения скорости
        burn_amount = input("Сколько сжечь топлива для снижения скорости: ")
        burn_amount = int(burn_amount)

        docking_sequence.perform_burn(burn_amount)
        docking_sequence.update_distance()

        # Проверка на успешное завершение игры. Если все условия выполнены, то игра пройдена
        if docking_sequence.distance <= 11 and docking_sequence.speed <= docking_sequence.distance:
            print("Стыковка подтвержена. Поздравляем экипаж!")
        else:
            print("Миссия провалена. Союз Т-6 не смог состыковаться с Салют-7")


main()