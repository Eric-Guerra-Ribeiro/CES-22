import abc

class Vehicle(abc.ABC):
    """
    Class that represents an abstract vehicle.
    """
    def __init__(self, engine, mass) -> None:
        self.engine = engine
        self.velocity = 0
        self.mass = mass
    
    def accelerate(self):
        """
        Acceleartes the vehicle.
        """
        self.velocity += self.engine.accelerate()/self.mass

    def breaking(self):
        """
        Breakes the vehicle.
        """
        self.engine.stop()
        self.velocity = 0
    
    def __str__(self) -> str:
        return f"{self.engine}."


class Car(Vehicle):
    """
    Class that represents a car.
    """
    def __init__(self, engine, mass) -> None:
        super().__init__(engine, mass)
    
    def __str__(self) -> str:
        return "Car with " + super().__str__()


class Truck(Vehicle):
    """
    Class that represents a truck.
    """
    def __init__(self, engine, mass) -> None:
        super().__init__(engine, mass)
    
    def __str__(self) -> str:
        return "Truck with " + super().__str__()


class Engine(abc.ABC):
    """
    Class that represents an engine.
    """
    def __init__(self) -> None:
        super().__init__()
    
    @abc.abstractmethod
    def accelerate(self):
        """
        Accelerates the engine.
        """
        pass

    @abc.abstractmethod
    def stop(self):
        """
        Stops the engine.
        """
        pass


class EletricEngine(Engine):
    """
    Class that represents an eletric engine.
    """
    def __init__(self) -> None:
        super().__init__()
        self.charge = 1
        self.rotations = 600
    
    def accelerate(self):
        if self.charge > 0:
            self.rotations += 100
            acceleration = 500*self.rotations*(max(0.01 - self.charge, 0.01))
            self.charge = max(0, self.charge - 0.01)
            return acceleration
    
    def stop(self):
        self.rotations = 600
    
    def recharge(self):
        """
        Charges the engine charge.
        """
        self.charge = 1
    
    def __str__(self) -> str:
        return "Eletric Engine"


class HybridEngine(Engine):
    """
    Class that represents a hybrid engine.
    """
    def __init__(self) -> None:
        super().__init__()
        self.fuel = 1
        self.charge = 1
        self.rotations = 800
    
    def accelerate(self):
        if self.charge > 0:
            self.rotations += 100
            acceleration = 500*self.rotations*(max(0.01 - self.charge, 0.01))
            self.charge = max(0, self.charge - 0.01)
            return acceleration
        if self.fuel > 0:
            self.rotations += 100
            acceleration = 500*self.rotations*0.05
            self.fuel = max(0, self.fuel - 0.01)
            return acceleration
    
    def stop(self):
        self.rotations = 800
    
    def refuel(self):
        """
        Refuel the engine tank.
        """
        self.fuel = 1

    def recharge(self):
        """
        Recharges the engine charge.
        """
        self.charge = 1
    
    def __str__(self) -> str:
        return "Hybrid Engine"


class CombustionEngine(Engine):
    """
    Class that represents an eletric engine.
    """
    def __init__(self) -> None:
        super().__init__()
        self.fuel = 1
        self.charge = 1
        self.rotations = 1200
    
    def accelerate(self):
        if self.fuel > 0:
            self.rotations += 100
            acceleration = 1000*self.rotations*0.05
            self.fuel = max(0, self.fuel - 0.01)
            return acceleration
    
    def stop(self):
        self.rotations = 1200
    
    def refuel(self):
        """
        Refuel the engine tank.
        """
        self.fuel = 1
    
    def __str__(self) -> str:
        return "Combustion Engine"

class VehicleFactory(abc.ABC):
    """
    Vehicle Factory
    """
    @abc.abstractstaticmethod
    def make_eletric_engine_vehicle(mass):
        """
        Makes an engine with an eletric engine.
        """
        pass

    @abc.abstractstaticmethod
    def make_eletric_hybrid_vehicle(mass):
        """
        Makes an engine with a hybrid engine.
        """
        pass

    @abc.abstractstaticmethod
    def make_eletric_combustion_vehicle(mass):
        """
        Makes an engine with a combustion engine.
        """
        pass

class CarFactory(VehicleFactory):
    """
    Car Factory
    """
    @abc.abstractstaticmethod
    def make_eletric_engine_vehicle(mass):
        return Car(EletricEngine(), mass)

    @abc.abstractstaticmethod
    def make_eletric_hybrid_vehicle(mass):
        return Car(HybridEngine(), mass)

    @abc.abstractstaticmethod
    def make_eletric_combustion_vehicle(mass):
        return Car(CombustionEngine(), mass)

class TruckFactory(abc.ABC):
    """
    Truck Factory
    """
    @abc.abstractstaticmethod
    def make_eletric_engine_vehicle(mass):
        return Truck(EletricEngine(), mass)

    @abc.abstractstaticmethod
    def make_eletric_hybrid_vehicle(mass):
        return Truck(HybridEngine(), mass)

    @abc.abstractstaticmethod
    def make_eletric_combustion_vehicle(mass):
        return Truck(CombustionEngine(), mass)

if __name__ == "__main__":
    Tesla = CarFactory.make_eletric_engine_vehicle(1000)
    for i in range(3):
        Tesla.accelerate()
    Tesla.breaking()
    print(Tesla)
    Semitruck = TruckFactory.make_eletric_combustion_vehicle(20000)
    for i in range(30):
        Semitruck.accelerate()
    Semitruck.breaking()
    print(Semitruck)
    Prius = CarFactory.make_eletric_hybrid_vehicle(900)
    Prius.accelerate()
    Prius.breaking()
    print(Prius)
