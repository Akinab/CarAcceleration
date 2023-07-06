def details ():
    Description = "Car Acceleration"
    Date = "06-07-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

# Create a Car object
car = Car(2023, "Example Make")

# Accelerate the car five times and display the current speed after each acceleration
for _ in range(5):
    car.accelerate()
    print("Current speed:", car.get_speed())
