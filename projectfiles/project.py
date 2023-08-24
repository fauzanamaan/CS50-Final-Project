import random
import tkinter as tk

# Global variables
COMPUTER_SCORE = 0
HUMAN_SCORE = 0

def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""
    global COMPUTER_SCORE, HUMAN_SCORE
    
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    human_choice_number = choices.index(human_choice)
    computer_choice_number = choices.index(computer_choice)
    
    if human_choice == computer_choice:
        result_text.set("It's a Tie!")
    elif (human_choice_number - computer_choice_number) % 3 == 1:
        result_text.set("Computer wins!")
        COMPUTER_SCORE += 1
    else:
        result_text.set("Human wins!")
        HUMAN_SCORE += 1
        
    update_scores()

def update_scores():
    human_score_label.config(text=f"Human Score: {HUMAN_SCORE}")
    computer_score_label.config(text=f"Computer Score: {COMPUTER_SCORE}")

def play(choice):
    choice_result(choice, random.choice(['rock', 'paper', 'scissors']))

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg='#F2F2F2')

# Create labels
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 20), fg='#333333', bg='#F2F2F2')
result_label.pack(pady=20)

human_score_label = tk.Label(root, text="Human Score: 0", font=("Helvetica", 16), fg='#007ACC', bg='#F2F2F2')
human_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Helvetica", 16), fg='#FF5733', bg='#F2F2F2')
computer_score_label.pack()

# Create a frame to hold buttons
button_frame = tk.Frame(root, bg='#F2F2F2')
button_frame.pack()

# Create buttons
choices = ['rock', 'paper', 'scissors']
for choice in choices:
    button = tk.Button(button_frame, text=choice.capitalize(), command=lambda c=choice: play(c), font=("Helvetica", 14), padx=20, pady=10)
    button.pack(side=tk.LEFT)

# Center-align buttons
button_frame.update()
frame_width = button_frame.winfo_width()
button_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
