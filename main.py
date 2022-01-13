from tkinter import *
from tkinter import messagebox


# Inialize the window
window = Tk()

# Set the screen title 
window.title("TicTacToe")


# handle turn
clicked = True
count = 0


# disable all the buttons
def terminate_the_board():
    
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    
    #messagebox.showinfo("Game End", "Game has been end.")

# Check if someone won
def check_game_status():
    global winner
    winner = False
    
    ### CHECK FOR 'X' WIN
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":

        b1.config(bg="Green")
        b2.config(bg="Green")
        b3.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":

        b4.config(bg="Green")
        b5.config(bg="Green")
        b6.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()
    
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":

        b7.config(bg="Green")
        b8.config(bg="Green")
        b9.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":

        b1.config(bg="Green")
        b4.config(bg="Green")
        b7.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":

        b2.config(bg="Green")
        b5.config(bg="Green")
        b8.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":

        b3.config(bg="Green")
        b6.config(bg="Green")
        b9.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":

        b1.config(bg="Green")
        b5.config(bg="Green")
        b9.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":

        b3.config(bg="Green")
        b5.config(bg="Green")
        b7.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "X, Won!")
        terminate_the_board()

    ### CHECK FOR 'O' wins

    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":

        b1.config(bg="Green")
        b2.config(bg="Green")
        b3.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":

        b4.config(bg="Green")
        b5.config(bg="Green")
        b6.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()
    
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":

        b7.config(bg="Green")
        b8.config(bg="Green")
        b9.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":

        b1.config(bg="Green")
        b4.config(bg="Green")
        b7.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":

        b2.config(bg="Green")
        b5.config(bg="Green")
        b8.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":

        b3.config(bg="Green")
        b6.config(bg="Green")
        b9.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":

        b1.config(bg="Green")
        b5.config(bg="Green")
        b9.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":

        b3.config(bg="Green")
        b5.config(bg="Green")
        b7.config(bg="Green")
        winner = True

        messagebox.showinfo("TicTacToe", "O, Won!")
        terminate_the_board()


# Button functions
def b_clicked(b):
    global clicked, count


    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        
        # CHECK IF SOMEONE WIN OR NOT
        check_game_status()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        
        # CHECK IF SOMEONE WIN OR NOT
        check_game_status()

    else:

        messagebox.showerror("TicTacToe", "Hey the box is not avaible.")




# Build the buttons
b1 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b1))
b2 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b2))
b3 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b3))

b4 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b4))
b5 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b5))
b6 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b6))

b7 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b7))
b8 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b8))
b9 = Button(window, text=" ", font=("Helvetica", 20), width=5, height=5, bg="white", fg="black", command=lambda: b_clicked(b9))




# Set the Grid value for the buttons and display into screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


window.mainloop()



