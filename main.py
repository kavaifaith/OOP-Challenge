from pet import Pet  # assuming the Pet class is in a file named pet.py

def main():
    # Create a pet object
    my_pet = Pet("Fluffy")  # You can name your dog anything you like

    # Call methods to test functionality
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("Shake Hands")
    my_pet.train("Fetch")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
