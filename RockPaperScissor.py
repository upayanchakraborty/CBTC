import random
rps = ["rock", "paper", "scissors"]
cmove = random.choice(rps)
umove = input("Enter a choice (rock, paper, scissors): ")
print("\nYou chose ",umove, "computer chose",cmove,".\n")

if umove == cmove:
    print("Both players selected ",umove,". It's a tie!")
elif umove == "rock":
    if cmove == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif umove == "paper":
    if cmove == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif umove == "scissors":
    if cmove == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")