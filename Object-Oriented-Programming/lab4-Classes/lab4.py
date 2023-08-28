#1
from math import pi

class sphereCalci():
	def __init__(self, radius):
		self.radius = radius
		

	def surfaceArea(self):
		return int(4 * pi * self.radius**2)


	def volume(self):
		return int(4/3 * pi * self.radius**3)

	def getradius(self):
		return self.radius
def main():
	radius = sphereCalci(5)

	print('Surface Area:',radius.surfaceArea())
	print('volume:',radius.volume())
main()

#2

class playcard:

    def _init_(self, rank, suit):
        if (rank <= 13 or rank >= 1) and (suit == "d" or suit == "c" or suit == "h" or suit == "s"):
            self.rank = rank
            self.indicator = self.rank
            if suit == "d":
                self.suit = "Diamonds"
            elif suit == "c":
                self.suit = "Clubs"
            elif suit == "h":
                self.suit = "Hearts"
            else:
                self.suit = "Spades"

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        if self.rank >= 11:
            return 10
        else:
            return self.rank

    def _str_(self):
        if self.rank == 1:
            self.indicator = "Ace"
        elif self.rank == 11:
            self.indicator = "Jack"
        elif self.rank == 12:
            self.indicator = "Queen"
        elif self.rank == 13:
            self.indicator = "King"

        return str(self.indicator) + " of " + self.suit

import random

def main(n):
    shade = ["d", "c", "h", "s"]
    for i in range(n):
        cards = playcard(random.randint(1, 13), shade[random.randint(0,len(shade)-1)])
        print(cards)
        print("Blackjack value of card", cards.BJValue())

main(6)


#3
class customer():

	def __init__(self,id,currentbalance,accountid):
		self.id= id
		self.currentbalance = currentbalance
		self.accountid = accountid

	def displayinfo(self):
		print(self.id,self.currentbalance,self.accountid)
def main():
	ethen = customer(789,89000,80099)
	fred = customer(657,990000,70088)
	ethen.displayinfo()
	fred.displayinfo()


main()