
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
        start = 0  # Grenze einfügen
        # wenn ein print gegeben dann sieht man den gewürfelte Zahl
        rolled_number = random.randint(start, limit)
        # Ein_Zahl=None um den while schleife immer den input drückt bis das Ziel
        self.In_number = None
        counter = 0  # um den Zähler der Schleife zu darstellen
        maxi_win = 3
        while self.In_number != rolled_number:
            self.In_number = int(input("Please enter your number betweent 0 and 100 : "))
            if rolled_number == self.In_number:
                print("yaaaah, Ihre Zahl ist die richtige Zahl, :) Herzlichen Glückwunsch")
            elif rolled_number < self.In_number:
                print("Ihre Zahl ist größer als die richtige Zahl")
                counter = counter + 1
            else:
                print("Ihre Zahl ist kleiner als die richtige Zahl ): ")
                counter = counter + 1
        print(" Sie haben " + str(counter) + " Versuche benötigt")

        if counter <= maxi_win:
            print("Sie haben 100$ gewonnen vom Automat")
        else:
            print("Versuchen Sie bitte mit weniger als " + str(maxi_win) + " Versuchen um Geld zu erhalten")

c1 = Game()


