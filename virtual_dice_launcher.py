import random

def roll_dice(sides=6):
    return random.randint(1, sides)

if __name__ == "__main__":
    print("Dice Roller")
    sides = int(input("Enter number of sides on the dice: "))
    print(f"You rolled: {roll_dice(sides)}")