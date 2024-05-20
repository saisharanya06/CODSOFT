import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", width=20, command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(self.root, text="Paper", width=20, command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", width=20, command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="User: 0, Computer: 0", font=('Helvetica', 14))
        self.score_label.pack(pady=10)
        
        self.play_again_button = tk.Button(self.root, text="Play Again", width=20, command=self.reset_game)
        self.play_again_button.pack(pady=5)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"User: {user_choice},\n Computer: {computer_choice}\n{result}")
        
        self.score_label.config(text=f"User: {self.user_score},\n Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="User: 0, Computer: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
