print("Welcome To The Game!")
print("********************")
num_left = 13
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")


def get_valid_choice(player_name):
    while True:
        try:
            choice = int(input(f"{player_name}, how many toothpicks do you take? "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    p1_choice = get_valid_choice(player1_name)
    num_left -= p1_choice
    if num_left <= 0:
        print(f"{player1_name} wins the game!")
        break

    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    p2_choice = get_valid_choice(player2_name)
    num_left -= p2_choice
    if num_left <= 0:
        print(f"{player2_name} wins the game!")
        break

print("GAME OVER!")