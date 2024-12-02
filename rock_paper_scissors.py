import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("Choose rock, paper, or scissors: ").lower()
    
    if player not in choices:
        print("Invalid choice!")
    elif player == computer:
        print(f"Draw! Both chose {player}.")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print(f"You win! {player} beats {computer}.")
    else:
        print(f"You lose! {computer} beats {player}.")

if __name__ == "__main__":
    play_game()