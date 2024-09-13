class car:
    brand = ""
    model = ""

    def show(self):
        print(f"Car:{self.brand} {self.model}")
my_car = car()

my_car.brand = "abc"
my_car.model = "xyz"

my_car.show()