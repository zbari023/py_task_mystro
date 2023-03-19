
# Two Games in this class
import random  # to get rolled number
class Game:
    def __init__(self):
        while True:
            print('Welcome in Python Game ,press 0 to exit of game')
            user = eval(input('Enter your Game Number 1 or 2 : '))

            if user == 1:
                print("Max of 2 values: ")
                x = int(input('Enter your first Number:  '))
                y = int(input('Enter your second Number:  '))
                self.Maximum(x, y)
                print("End of game 1")
            elif user == 2:
                print(" A Game to chose a number between 0 and 100 with less than 3 tries to get 100$ ")
                self.money_game()
                print("End of game 2")
            elif user == 0:    # to exit of the game and to be the end
                print("Thank you to your play")
                exit()
            else:
                pass





    def Maximum(self, x, y):
        self.x = x
        self.y = y
        if self.x > self.y:
            print(f"{self.x} > {self.y}")
        elif self.x == self.y:
            print(f"{self.x} = {self.y}")
        else:
            print(f"{self.y} > {self.x} ")
    def money_game(self):
        limit = 100
        start = 0  # Insert Boundary
        # if a print given then you see the rolled number
        rolled_number = random.randint(start, limit)
        # In_number=None around the while loop always presses the input until the target
        self.In_number = None
        counter = 0  # to display the counter of the loop
        maxi_win = 3
        while self.In_number != rolled_number:
            self.In_number = int(input("Please enter your number between 0 and 100 : "))
            if rolled_number == self.In_number:
                print("yaaaah, your number is the right number, :) Congratulations")
            elif rolled_number < self.In_number:
                print("Your number is greater than the correct number desired")
                counter = counter + 1
            else:
                print("Your number is less than the correct number ):")
                counter = counter + 1
        print(" you needed " + str(counter+1) + " tries" )

        if counter <= maxi_win:
            print("You have won 100$ from the slot machine")
        else:
            print("Please try with less than " + str(maxi_win) + " tries to get money")

c1 = Game()


