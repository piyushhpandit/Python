winning_num = int (50)
guessed_num = int(input("enter a number : "))
if winning_num == guessed_num:
    print("YOU WIN")
else:
    if winning_num > guessed_num:
        print("You guessed too low")
    if winning_num < guessed_num:
        print("You guessed too high")
    else:
        pass


