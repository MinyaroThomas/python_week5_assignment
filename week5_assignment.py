# Task 1: Design Your Own Class! (Superhero with Inheritance and Encapsulation)
class Superhero:
    def __init__(self, name, power, energy_level):
        self.name = name
        self.power = power
        self.__energy_level = energy_level  # Private attribute (encapsulation)

    def use_power(self):
        if self.__energy_level >= 10:
            print(f"{self.name} uses their {self.power} power!")
            self.__energy_level -= 10
            print(f"Energy level is now: {self.__energy_level}")
        else:
            print(f"{self.name} is too tired to use their power. Energy level: {self.__energy_level}")

    def rest(self):
        self.__energy_level += 20
        if self.__energy_level > 100:
            self.__energy_level = 100
        print(f"{self.name} rests and regains energy. Energy level is now: {self.__energy_level}")

    def get_energy_level(self):  # Getter method for private attribute
        return self.__energy_level

    def move(self):  # This method will be overridden in the child class (for polymorphism)
        print(f"{self.name} moves by running!")


class FlyingSuperhero(Superhero):  # Inheritance
    def __init__(self, name, power, energy_level, flying_speed):
        super().__init__(name, power, energy_level)  # Call parent class constructor
        self.flying_speed = flying_speed

    def fly(self):
        print(f"{self.name} flies at a speed of {self.flying_speed} km/h!")

    def move(self):  # Override the move method (polymorphism)
        print(f"{self.name} moves by flying at {self.flying_speed} km/h!")


# Task 2: Polymorphism Challenge! (Animals with different move behaviors)
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves!")  # Generic move method to be overridden


class Dog(Animal):
    def move(self):  # Override move method
        print(f"{self.name} moves by running on four legs!")


class Bird(Animal):
    def move(self):  # Override move method
        print(f"{self.name} moves by flying in the sky!")


# Functions to demonstrate polymorphism
def demonstrate_animal_movement(animal):
    animal.move()


def demonstrate_superhero_movement(superhero):
    superhero.move()


# Main program to demonstrate both tasks
if __name__ == "__main__":
    print("=== Task 1: Design Your Own Class! ===")
    # Create a regular superhero
    hero1 = Superhero("Captain Strength", "Super Strength", 50)
    print(f"{hero1.name}'s initial energy: {hero1.get_energy_level()}")
    hero1.use_power()
    hero1.rest()
    hero1.move()

    # Create a flying superhero (inheritance)
    hero2 = FlyingSuperhero("Sky Blazer", "Laser Vision", 70, 300)
    print(f"\n{hero2.name}'s initial energy: {hero2.get_energy_level()}")
    hero2.use_power()
    hero2.fly()
    hero2.move()

    print("\n=== Task 2: Polymorphism Challenge! ===")
    # Create animals
    dog = Dog("Rex")
    bird = Bird("Tweety")

    # Demonstrate polymorphism with animals
    print("Animal Movements:")
    demonstrate_animal_movement(dog)
    demonstrate_animal_movement(bird)

    # Demonstrate polymorphism with superheroes
    print("\nSuperhero Movements:")
    demonstrate_superhero_movement(hero1)
    demonstrate_superhero_movement(hero2)