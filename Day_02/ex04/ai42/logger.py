import time
from random import randint
import os


def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        elapsed = float(time.time() - start)
        if elapsed > 1:
            unit = "s"
        else:
            elapsed *= 1000
            unit = "ms"
        if "USER" in os.environ:
            user = os.environ["USER"]
        else:
            user = "User_not_found"
        func_name = func.__name__.capitalize()
        logline = "({user})Running: {func_name:<20}[exec-time = {elapsed:.3f}" \
                  "{unit:<3}]\n".format(user=user, func_name=func_name,
                                        elapsed=elapsed, unit=unit)
        logfile = open("machine.log", "a")
        logfile.write(logline)
        logfile.close()
        return res

    return wrapper


class CoffeeMachine:
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
