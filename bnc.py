from random import randint
#define roles
roles = ["Bear", "Ninja", "Cowboy"]
# Generate a random role using an array
computer = roles[randint(0,2)]


player = False

while player == False:
    player = input("Bear, Ninja, or Cowboy? > ")
    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", computer, "shoots", player)
        else: #computer is cowboy, plyer is Ninja
            print("You win!", player, "slices", computer)
    elif computer == "Bear":
        if player == "Ninja":
            print("You lose!", computer, "eats", player)
        else: #computer is bear, plyer is cowboy
            print("You win!", player, "shoots", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", computer, "slices", player)
        else: #computer is ninja, plyer is bear
            print("You win!", player, "shoots", computer)
    else:
     print(computer, player)
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
            player = False
