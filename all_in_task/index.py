
# comming soon
class Game:
    def __init__(self):
        print('Welcome in Python Game')
        user = eval(input('Enter your Game Number: '))

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

c1 = Game()
c1.Maximum(33,7)

