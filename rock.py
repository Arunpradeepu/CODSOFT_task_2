import tkinter as tk
import random
from tkinter import messagebox

player_score = 0
computer_score = 0
round_count = 0

def play(user_choice):
    global player_score, computer_score, round_count
    
    if round_count >= 10:
        
        messagebox.showinfo("Game Over","You have played 10 rounds. \nGame over!" )
        return
    
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
        player_score += 1
        computer_score += 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 2
        result = "You win!"
    else:
        computer_score += 2
        result = "You lose!"
    

    
    round_count += 1    
    
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result} \nYour score: {player_score} \nComputer's score: {computer_score} \nRound: {round_count}/10")


app = tk.Tk()
app.title("Stone-Paper-Scissors")
app.resizable(False,False)
app.geometry("400x600")
app.configure(bg="#F08080")


tk.Label( text="ROCK-PAPPER-SCISSORS",background="#f08080",font=("san-serif", 20)).pack(pady=20)
tk.Label( text="IF PLAYER WINS : 2 POINTS",background="#f08080",font=("san-serif",10)).pack(pady=10)
tk.Label( text="IF PLAYER LOSS : 0 POINTS",background="#f08080",font=("san-serif",10)).pack(pady=5)
tk.Label( text="IF MATCH TIED : 1 POINT",background="#f08080",font=("san-serif",10)).pack(pady=5)

button_frame = tk.Frame(app)
button_frame.pack()

top = tk.PhotoImage(file="stone.png")
tk.Label(app, image=top,bg="#F08080").place(x=30,y=350)

note= tk.PhotoImage(file="paper.png")
tk.Label(app, image=note ,bg="#F08080").place(x=180,y=370)

sis= tk.PhotoImage(file="sis.png")
tk.Label(app, image=sis ,bg="#F08080").place(x=300,y=380)


rock_button = tk.Button(button_frame, text="Rock", width=10,font=("san-serif", 15), command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10,font=("san-serif", 15),command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, font=("san-serif", 15),command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)


result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack(pady=20)



app.mainloop()
