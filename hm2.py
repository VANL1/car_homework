class collector:
    pass


class engine:
    def __init__(self, mass, speed, fuel_consumption):
        self.mass = mass
        self.speed = speed
        self.fuel_consumption = fuel_consumption


class tank:
    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume


class brakes:
    def __init__(self, mass, effect):
        self.mass = mass
        self.effect = effect


class body:
    def __init__(self, mass):
        self.mass = mass


class car:

    def __init__(self, name, engine, tank, brakes, body):
        self.mass = engine.mass + tank.mass + brakes.mass + body.mass
        self.name = name
        self.engine = engine
        self.tank = tank
        self.brakes = brakes
        self.body = body
        self.max_course=tank.volume*engine.speed*engine.fuel_consumption
        self.brakes_course=(self.mass/brakes.effect)*100



engine1 = engine(100, 200, 10)
tank1 = tank(100, 50)
brakes1 = brakes(100, 100)
body1 = body(100)
car1 = car("Toyoto", engine1, tank1, brakes1, body1)

print(car1.name)
print(car1.mass_sum())
print(car1.max_course)
print(car1.brakes_course)
