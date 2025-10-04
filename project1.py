class Car:
    """Base class for all cars"""
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def start_engine(self):
        raise NotImplementedError("Subclass must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Subclass must implement this method")
    
    def get_info(self):
        raise NotImplementedError("Subclass must implement this method")

class BMW(Car):
    """BMW class inheriting from Car"""
    def __init__(self, model, year, price, series):
        super().__init__(model, year, price)
        self.series = series
        self.engine_started = False
    
    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            return f"BMW {self.model} engine started with iDrive system"
        return f"BMW {self.model} engine is already running"
    
    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            return f"BMW {self.model} engine stopped gracefully"
        return f"BMW {self.model} engine is already off"
    
    def get_info(self):
        return f"BMW {self.model} Series {self.series} ({self.year}) - ${self.price:,}"
    
    def enable_sport_mode(self):
        return f"BMW {self.model} Sport Mode activated!"

class Ferrari(Car):
    """Ferrari class inheriting from Car"""
    def __init__(self, model, year, price, top_speed):
        super().__init__(model, year, price)
        self.top_speed = top_speed
        self.engine_started = False
    
    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            return f"Ferrari {self.model} engine ROARS to life! 🏎️"
        return f"Ferrari {self.model} engine is already ROARING!"
    
    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            return f"Ferrari {self.model} engine purrs to silence"
        return f"Ferrari {self.model} engine is already silent"
    
    def get_info(self):
        return f"Ferrari {self.model} ({self.year}) - ${self.price:,} - Top Speed: {self.top_speed} mph"
    
    def launch_race_mode(self):
        return f"Ferrari {self.model} Race Mode ENGAGED! 🚀"

# Demonstration of polymorphism
def demonstrate_polymorphism():
    print("🚗 CAR SHOWROOM - POLYMORPHISM DEMONSTRATION 🚗")
    print("=" * 50)
    
    # Create instances
    bmw_m5 = BMW("M5", 2023, 105000, "5")
    ferrari_sf90 = Ferrari("SF90 Stradale", 2023, 625000, 211)
    
    # List of cars - polymorphism in action!
    cars = [bmw_m5, ferrari_sf90]
    
    # Same interface, different behaviors
    for car in cars:
        print(f"\n{car.get_info()}")
        print("-" * 40)
        
        # These methods work the same way for both classes
        print(car.start_engine())
        print(car.stop_engine())
        
        # Class-specific methods
        if isinstance(car, BMW):
            print(car.enable_sport_mode())
        elif isinstance(car, Ferrari):
            print(car.launch_race_mode())

# Run the demonstration
demonstrate_polymorphism()