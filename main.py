# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

# Create and open GUI window
app_window = tkinter.Tk()
app_window.title("Password Manager")
app_window.minsize(width=300, height=300)
app_window.config(padx=20, pady=20)

# Display Logo
app_logo = tkinter.PhotoImage(file="logo.png")
logo_canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_canvas.create_image(125, 125, image=app_logo)
logo_canvas.grid(row=2, column=2)

# Exit GUI window
app_window.mainloop()