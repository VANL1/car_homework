# Cборщик, не знаю зачем -_-
class collector:
    @staticmethod
    def buildcar(name, engine, tank, brakes, body):
        return car(name, engine, tank, brakes, body)


# Двигатель
class engine:
    def __init__(self, mass, speed, fuel_consumption):  # Просто вызов функции
        self.mass = mass  # Масса двигателя
        self.speed = speed  # Максимальная скорость
        self.fuel_consumption = fuel_consumption  # Расход топлива в час


# Бак
class tank:
    def __init__(self, mass, volume):  # Просто ещё один вызов функции
        self.mass = mass  # Масса бака
        self.volume = volume  # Объём бака


# Тормоза
class brakes:
    def __init__(self, mass, effect):  # И опять вызов функции
        self.mass = mass  # Масса тормозов
        self.effect = effect  # Эффективность тормозов


# Кузов
class body:
    def __init__(self, mass):  # И снова вызов функции
        self.mass = mass  # Масса кузова


# Сама машина
class car:
    def __init__(self, name, engine, tank, brakes, body):  # Угадайте что? Да, вызов функции...
        self.mass = engine.mass + tank.mass + brakes.mass + body.mass  # Общяя масса автомобиля
        self.name = name  # Марка машины
        self.engine = engine  # Вызов двигателя
        self.tank = tank  # Вызов бака
        self.brakes = brakes  # Вызов торомозов
        self.body = body  # Вызов кузова
        self.max_course = (tank.volume * engine.speed) / engine.fuel_consumption  # Максимальный запас хода
        self.brakes_course = (self.mass / brakes.effect) * 100  # Торозной путь


name1 = "Toyoto"  # Первая марка
name2 = "BMW"  # Вторая марка
engine1 = engine(100, 200, 10)  # Двигатель с массой 100кг, макс.скоростью 200 км/ч и расходом 10 л/ч
engine2 = engine(150, 300, 9)  # Двигатель №2 с массой 100, макс.скоростью 300 км/ч и расходом 10 л/ч
tank1 = tank(100, 50)  # Бак с массой 100кг и объёмом 50л
brakes1 = brakes(100, 100)  # Тормоза массой 100кг и эффективностью 100(т/м???)
body1 = body(100)  # Кузов массой 100
car1 = car(name1, engine1, tank1, brakes1, body1)  # Машина №1 марки Toyoto
car2 = car(name2, engine2, tank1, brakes1, body1)  # Машина №2 марки BMW

print(collector.buildcar(name1, engine1, tank1, brakes1, body1))  # Попытка вызова сборщика (Сполейр не удачная)

print('Марка:', car1.name)
print("Масса:", car1.mass)
print("Макс запас хода:", car1.max_course)
print("Тормозной путь:", car1.brakes_course)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")  # Тут весь вывод с описанием (можно поигарть со значениями )
print('Марка:', car2.name)
print("Масса:", car2.mass)
print("Макс запас хода:", car2.max_course)
print("Тормозной путь:", car2.brakes_course)
