import random
import tkinter as tk
from tkinter import messagebox

def getCardValue():
    return random.randint(2, 14)

def getCardStr(cardValue):
    if 2 <= cardValue <= 9:
        return str(cardValue)
    elif cardValue == 10:
        return "T"
    elif cardValue == 11:
        return "J"
    elif cardValue == 12:
        return "Q"
    elif cardValue == 13:
        return "K"
    elif cardValue == 14:
        return "A"
    else:
        raise ValueError("cardValue must be between 2 and 14")

def playerGuessCorrect(card1, card2, betType):
    if card1 == card2:
        return False
    elif betType == "HIGH":
        return card2 > card1
    elif betType == "LOW":
        return card2 < card1
    else:
        raise ValueError("betType must be either 'HIGH' or 'LOW'")

class HighLowGame:
    def __init__(self, root):
        self.root = root
        self.root.title("High-Low Card Game")

        # Game variables
        self.points = 100
        self.round_num = 0
        self.max_rounds = 10
        self.card1 = None
        self.card2 = None
        self.betType = None

        # GUI Elements
        self.label_points = tk.Label(root, text=f"Points: {self.points}")
        self.label_points.pack()

        self.label_card1 = tk.Label(root, text="First Card: N/A")
        self.label_card1.pack()

        self.bet_frame = tk.Frame(root)
        self.bet_frame.pack()

        self.label_bet = tk.Label(self.bet_frame, text="Bet amount (1-100):")
        self.label_bet.pack(side=tk.LEFT)
        self.entry_bet = tk.Entry(self.bet_frame)
        self.entry_bet.pack(side=tk.LEFT)

        self.btn_high = tk.Button(root, text="High", command=lambda: self.play_round("HIGH"))
        self.btn_high.pack(side=tk.LEFT)

        self.btn_low = tk.Button(root, text="Low", command=lambda: self.play_round("LOW"))
        self.btn_low.pack(side=tk.LEFT)

        self.label_card2 = tk.Label(root, text="Second Card: N/A")
        self.label_card2.pack()

        self.label_result = tk.Label(root, text="")
        self.label_result.pack()

    def play_round(self, betType):
        if self.round_num >= self.max_rounds or self.points <= 0 or self.points >= 500:
            messagebox.showinfo("Game Over", "Game over! Please restart the game.")
            return

        try:
            betAmount = int(self.entry_bet.get())
            if betAmount < 1 or betAmount > self.points:
                messagebox.showwarning("Invalid Bet", "Invalid bet amount.")
                return
        except ValueError:
            messagebox.showwarning("Invalid Bet", "Please enter a valid bet amount.")
            return

        self.card1 = getCardValue()
        self.label_card1.config(text=f"First Card: {getCardStr(self.card1)}")

        self.betType = betType
        self.card2 = getCardValue()
        self.label_card2.config(text=f"Second Card: {getCardStr(self.card2)}")

        if playerGuessCorrect(self.card1, self.card2, self.betType):
            self.label_result.config(text="Correct guess!", fg="green")
            self.points += betAmount
        else:
            self.label_result.config(text="Wrong guess!", fg="red")
            self.points -= betAmount

        self.round_num += 1
        self.label_points.config(text=f"Points: {self.points}")

        if self.points >= 500:
            messagebox.showinfo("Congratulations", f"You won with {self.points} points!")
        elif self.points <= 0:
            messagebox.showinfo("Game Over", f"You lost all your points in round {self.round_num}!")

if __name__ == "__main__":
    root = tk.Tk()
    game = HighLowGame(root)
    root.mainloop()
