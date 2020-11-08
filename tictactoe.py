import tkinter as tk
import random



class guiPart():
	def __init__(self):
		self.money = 100
		self.moneyLabel = tk.Label(gui, text = "Money: "+str(self.money))
		self.stateLabel = tk.Label(gui, text = "")
		self.dealerLabel = tk.Label(gui, text = "Dealer: ")
		self.playerLabel = tk.Label(gui, text = "Player: ")
		self.playerHand = []
		self.dealerHand = []
		self.dealerLabels = []
		self.playerLabels = []
		self.standButton = tk.Button(gui, text="Stand", command=lambda: stand())
		self.hitButton = tk.Button(gui, text="Hit", command=lambda: hit())
		self.resetButton = tk.Button(gui, text="Reset", command=lambda: reset() )

def draw():
	r = random.random()
	card = int (r * 13 + 1)
	return card


def checkValue(card):
	if card == 1:
		return 1
	elif card > 10:
		return 11
	return card
def name(card):
	#split() makes an array of the words in the string
	names = "Joker Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King".split()

	return names[card]

def hasAce(hand):
	for card in hand :
		if card == "Ace" :
			return True
	return False

def hardSum(hand):
	total = 0
	totalAces = 0
	for card in hand:
		if card == "Ace" and totalAces != 0:
			total = total + 1
		else:
			total = total + checkValue(card)
	return total

def softSum(hand):
	total = 0
	totalAces = 0
	for card in hand:
		if card == "Ace" :
			total = total + 1
		else:
			total = total + checkValue(card)
	return total
def sum(hand):
	soft = softSum(hand)
	hard = hardSum(hand)
	if hard > soft and hard < 22:
		return hard
	return soft
	
def string(hand):
	newString = ""
	for card in hand :
		newString = newString + name(card) + " "
	return newString
def busted(hand):
	sumHand = sum(hand)
	if sumHand > 21 :
		return True
		
	return False

def update():
	x = 0
	
	for card in guipart.dealerHand:
		guipart.dealerLabels.append(tk.Label(gui, image=iarray[card - 2]))
		guipart.dealerLabels[x].grid(row=1, column=x)
		x = x + 1
	x = 0
	for card in guipart.playerHand:
		guipart.playerLabels.append(tk.Label(gui, image=iarray[card - 2]))
		guipart.playerLabels[x].grid(row=5, column=x)
		x = x + 1

	guipart.moneyLabel = tk.Label(gui, text = "Money: "+str(guipart.money))
	guipart.moneyLabel.grid(row=10, column=0)

	
def hit():
	guipart.playerHand.append(draw())
	update()
	if busted(guipart.playerHand) :
		guipart.stateLabel.configure(text = "You Busted")
		guipart.hitButton.configure(state=tk.DISABLED)
		guipart.standButton.configure(state=tk.DISABLED)
		guipart.money = guipart.money - 10

def stand():
	while True:
		if hardSum(guipart.dealerHand) < 15 or softSum(guipart.dealerHand) < 6:
			guipart.dealerHand.append(draw())
			update()
			if busted(guipart.dealerHand) :
				guipart.stateLabel.configure(text = "Dealer Busted")
				guipart.hitButton.configure(state=tk.DISABLED)
				guipart.standButton.configure(state=tk.DISABLED)
				break
		else :
			gameState = False
			update()
			if sum(guipart.dealerHand) > sum(guipart.playerHand) :
				guipart.stateLabel.configure(text = "You Lost!")
				guipart.money = guipart.money - 10
			else :
				guipart.stateLabel.configure(text = "You Won!")
				guipart.money = guipart.money + 10
			guipart.hitButton.configure(state=tk.DISABLED)
			guipart.standButton.configure(state=tk.DISABLED)
			break

def reset():
	
	guipart.hitButton.configure(state=tk.NORMAL)
	guipart.standButton.configure(state=tk.NORMAL)
	guipart.stateLabel.configure(text="")
	#telling the grid to forget the grid spaces taken up by the label arrays
	for label in guipart.dealerLabels:
		label.grid_forget()

	for label in guipart.playerLabels:
		label.grid_forget()

	#resetting the arrays
	guipart.dealerLabels = []
	guipart.playerLabels = []

	#resetting the hand arrays
	guipart.playerHand = []
	guipart.dealerHand = []

	#appending to the hands and calling update
	guipart.playerHand.append(draw())
	guipart.playerHand.append(draw())
	guipart.dealerHand.append(draw())
	guipart.dealerHand.append(draw())
	update()
gui = tk.Tk()
gui.title("Blackjack")
gui.geometry("800x640+200+300")
gui.configure(background = '#35654d')

guipart = guiPart()

guipart.stateLabel.grid(row=3, column=0)
guipart.dealerLabel.grid(row=0, column=0)
guipart.playerLabel.grid(row=4, column=0)

image2 = tk.PhotoImage(file="clubs-2-75.png")
image3 = tk.PhotoImage(file="spades-3-75.png")
image4 = tk.PhotoImage(file="clubs-4-75.png")
image5 = tk.PhotoImage(file="hearts-5-75.png")
image6 = tk.PhotoImage(file="clubs-6-75.png")
image7 = tk.PhotoImage(file="clubs-7-75.png")
image8 = tk.PhotoImage(file="hearts-8-75.png")
image9 = tk.PhotoImage(file="clubs-9-75.png")
image10 = tk.PhotoImage(file="diamonds-10-75.png")
image11 = tk.PhotoImage(file="diamonds-j-75.png")
image12 = tk.PhotoImage(file="hearts-q-75.png")
image13 = tk.PhotoImage(file="spades-k-75.png")
image14 = tk.PhotoImage(file="diamonds-a-75.png")

iarray = [image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13, image14]



guipart.standButton.grid(row = 6, column = 1)
guipart.hitButton.grid(row = 6, column = 0)
guipart.resetButton.grid(row = 6, column = 2)
guipart.playerHand.append(draw())
guipart.playerHand.append(draw())
guipart.dealerHand.append(draw())
guipart.dealerHand.append(draw())
update()

gui.mainloop()
