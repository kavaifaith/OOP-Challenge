class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating... Yum!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap... Zzz!")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing fetch! and having fun!")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")

    def get_status(self):
        print(f"\n {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f" - {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

# Example usage:
my_dog = Pet("Fluffy")

my_dog.get_status()
my_dog.eat()
my_dog.play()
my_dog.sleep()
my_dog.train("Sit")
my_dog.train("Roll Over")
my_dog.show_tricks()
my_dog.get_status()
