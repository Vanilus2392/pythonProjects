from random import randrange


def game():
    pass
    
def main():
    player = int(input("Rock[0], Paper[1], Scissors[2]? "))
    computer = randrange(2)

    print(f"Computer: {computer}")

    if player < 0 or player > 2:
        print("Invalid option")
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("Computer wins!")
    elif (player == 1 and computer == 0) or (player == 2 and computer == 1) or (player == 0 and computer == 2):
        print("Player wins!")
    else:
        print("Draw!")

if __name__ == "__main__":
    main()
    