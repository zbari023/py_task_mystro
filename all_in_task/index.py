
# coming soon
import random
class Game:
    def __init__(self):
        print('Welcome in Python Game')
        user = eval(input('Enter your Game Number: '))

        if user == 1:
            x = int(input('Enter your first Number:  '))
            y = int(input('Enter your second Number:  '))
            self.Maximum(x,y)
        elif user == 2:
            self.money_game()
        else:
            return print('please chose the game number 1 or 2')

    def Maximum(self, x, y):
        print("Max of 2 values: ")
        self.x = x
        self.y = y
        if self.x > self.y:
            print(f"{self.x} > {self.y}")
        elif self.x == self.y:
            print(f"{self.x} = {self.y}")
        else:
            print(f"{self.y} > {self.x} ")
    def money_game(self):
        limit = 100;
        start = 0  # Insert Boundary
        # if a print given then you see the dice number
        rolled_number = random.randint(start, limit)
        # In_number=None around the while loop always presses the input until the target
        self.In_number = None
        counter = 0  # to display the counter of the loop
        maxi_win = 3
        while self.In_number != rolled_number:
            self.In_number = int(input("Please enter your number betweent 0 and 100 : "))
            if rolled_number == self.In_number:
                print("yaaaah, your number is the right number, :) Congratulations")
            elif rolled_number < self.In_number:
                print("Your number is greater than the correct number desired")
                counter = counter + 1
            else:
                print("Your number is less than the correct number ):")
                counter = counter + 1
        print(" you needed " + str(counter) + "tries" )

        if counter <= maxi_win:
            print("Sie haben 100$ gewonnen vom Automat")
        else:
            print("Versuchen Sie bitte mit weniger als " + str(maxi_win) + " Versuchen um Geld zu erhalten")

c1 = Game()


