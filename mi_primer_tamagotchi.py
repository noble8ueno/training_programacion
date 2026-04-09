#!/usr/bin/env python3

import time


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.alive = True

    def status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def feed(self):
        print(f"You feed {self.name}.")
        self.hunger = max(0, self.hunger - 2)

    def sleep(self):
        print(f"{self.name} goes to sleep.")
        self.energy = min(10, self.energy + 3)

    def play(self):
        print(f"You play with {self.name}.")
        self.happiness = min(10, self.happiness + 2)
        self.energy = max(0, self.energy - 1)

    def tick(self):
        """Time passes"""
        self.hunger += 1
        self.energy -= 1
        self.happiness -= 1

        if self.hunger >= 10 or self.energy <= 0 or self.happiness <= 0:
            self.alive = False

    def is_alive(self):
        return self.alive


class Game:
    def __init__(self):
        pet_name = input("Name your Tamagotchi: ")
        self.pet = Tamagotchi(pet_name)

    def menu(self):
        print("\nChoose an action:")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Status")
        print("5. Exit")

    def run(self):
        while self.pet.is_alive():
            self.menu()
            choice = input(">> ")

            if choice == "1":
                self.pet.feed()
            elif choice == "2":
                self.pet.sleep()
            elif choice == "3":
                self.pet.play()
            elif choice == "4":
                self.pet.status()
            elif choice == "5":
                print("Goodbye!")
                return
            else:
                print("Invalid option.")

            self.pet.tick()
            time.sleep(1)

        print(f"\n{self.pet.name} has passed away... Game Over.")


if __name__ == "__main__":
    game = Game()
    game.run()
