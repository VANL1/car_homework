class Collector:
    @staticmethod
    def build_car(name, engine, tank, brakes, body):
        """Создает и возвращает объект автомобиля."""
        return Car(name, engine, tank, brakes, body)


# Двигатель
class Engine:
    def __init__(self, mass, speed, fuel_consumption):
        """Инициализация двигателя."""
        self.mass = mass  # Масса двигателя
        self.speed = speed  # Максимальная скорость
        self.fuel_consumption = fuel_consumption  # Расход топлива в час


# Бак
class Tank:
    def __init__(self, mass, volume):
        """Инициализация бака."""
        self.mass = mass  # Масса бака
        self.volume = volume  # Объём бака


# Тормоза
class Brakes:
    def __init__(self, mass, effect):
        """Инициализация тормозов."""
        self.mass = mass  # Масса тормозов
        self.effect = effect  # Эффективность тормозов


# Кузов
class Body:
    def __init__(self, mass):
        """Инициализация кузова."""
        self.mass = mass  # Масса кузова


# Автомобиль
class Car:
    def __init__(self, name, engine, tank, brakes, body):
        """Инициализация автомобиля."""
        self.name = name  # Марка машины
        self.engine = engine  # Двигатель
        self.tank = tank  # Бак
        self.brakes = brakes  # Тормоза
        self.body = body  # Кузов
        self.mass = self.calculate_total_mass()  # Общая масса автомобиля
        self.max_course = self.calculate_max_course()  # Максимальный запас хода
        self.brakes_course = self.calculate_braking_distance()  # Тормозной путь

    def calculate_total_mass(self):
        """Вычисляет общую массу автомобиля."""
        return self.engine.mass + self.tank.mass + self.brakes.mass + self.body.mass

    def calculate_max_course(self):
        """Вычисляет максимальный запас хода."""
        return (self.tank.volume * self.engine.speed) / self.engine.fuel_consumption

    def calculate_braking_distance(self):
        """Вычисляет тормозной путь."""
        return (self.mass / self.brakes.effect) * 100

    def __str__(self):
        """Возвращает строковое представление автомобиля."""
        return (f"Марка: {self.name}\n"
                f"Масса: {self.mass} кг\n"
                f"Макс. запас хода: {self.max_course} км\n"
                f"Тормозной путь: {self.brakes_course} м")


# Создание компонентов для автомобилей
engine1 = Engine(100, 200, 10)  # Двигатель с массой 100кг, макс.скоростью 200 км/ч и расходом 10 л/ч
engine2 = Engine(150, 300, 9)  # Двигатель №2 с массой 150кг, макс.скоростью 300 км/ч и расходом 9 л/ч
tank1 = Tank(100, 50)  # Бак с массой 100кг и объёмом 50л
brakes1 = Brakes(100, 100)  # Тормоза массой 100кг и эффективностью 100
body1 = Body(100)  # Кузов массой 100кг

# Создание автомобилей
car1 = Collector.build_car("Toyota", engine1, tank1, brakes1, body1)
car2 = Collector.build_car("BMW", engine2, tank1, brakes1, body1)

# Вывод информации об автомобилях
print(car1)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(car2)