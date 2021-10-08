# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

LABEL_FONT = ("Arial", 12)
BUTTON_FONT = ("Arial", 10)

# Create and open GUI window
app_window = tkinter.Tk()
app_window.title("Password Manager")
app_window.minsize(width=500, height=350)
app_window.config(padx=20, pady=20)

# Logo
app_logo = tkinter.PhotoImage(file="logo.png")
logo_canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_canvas.create_image(100, 100, image=app_logo)
logo_canvas.grid(row=1, column=2)

# Labels
website_label = tkinter.Label(text="Website: ", font=LABEL_FONT)
website_label.grid(row=2, column=1)
username_label = tkinter.Label(text="Email/Username: ", font=LABEL_FONT)
username_label.grid(row=3, column=1)
password_label = tkinter.Label(text="Password: ", font=LABEL_FONT)
password_label.grid(row=4, column=1)

# Website Entry
website_entry = tkinter.Entry(width=36)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2, sticky="W")

# Username/Email Entry
username_entry = tkinter.Entry(width=36)
username_entry.grid(row=3, column=2, columnspan=2, sticky="W")

# Password Entry
password_entry = tkinter.Entry(width=28)
password_entry.grid(row=4, column=2, sticky="W")

# "Generate Password" button
generatepassword_button = tkinter.Button(text="Generate Password", font=BUTTON_FONT)
generatepassword_button.grid(row=4, column=3)

# "Add" button
addpassword_button = tkinter.Button(text="Add", width=36, font=BUTTON_FONT)
addpassword_button.grid(row=5, column=2, columnspan=2, sticky="W", pady=20)

# Exit GUI window
app_window.mainloop()
