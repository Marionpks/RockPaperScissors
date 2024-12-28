import tkinter as tk
from tkinter import messagebox
import random

# Game logic
choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")

# GUI setup
window = tk.Tk()
window.title("Rock Paper Scissors")

# Title label
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18, "bold"), pady=20)
title_label.pack()

# Buttons for choices
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Exit button
exit_button = tk.Button(window, text="Exit", font=("Arial", 12), command=window.quit, bg="red", fg="white")
exit_button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
