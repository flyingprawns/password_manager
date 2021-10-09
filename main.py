import tkinter
from tkinter import messagebox
import random
import json

LABEL_FONT = ("Arial", 12)
BUTTON_FONT = ("Arial", 10)
ENTRY_FONT = ("Arial", 10)
PASSWORDFILE_PATH = "./passwords.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    generated_password_list = []

    for char in range(nr_letters):
        generated_password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        generated_password_list.append(random.choice(symbols))
    for char in range(nr_numbers):
        generated_password_list.append(random.choice(numbers))

    random.shuffle(generated_password_list)
    generated_password = "".join(generated_password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def addpassword_button_click():
    # Retrieve user input
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # Make sure no fields are empty
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        if website == "":
            website_entry.focus()
        elif username == "":
            username_entry.focus()
        else:
            password_entry.focus()
        return
    # Format the new data
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    # Try to open the data file
    try:
        with open(PASSWORDFILE_PATH, mode="r") as data_file:
            pass
    # If no file exists, create a new file and save the data to it
    except FileNotFoundError:
        with open(PASSWORDFILE_PATH, mode="w") as data_file:
            json.dump(new_data, data_file, indent=4)
    # Otherwise, update and save the data
    else:
        with open(PASSWORDFILE_PATH, mode="r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
        with open(PASSWORDFILE_PATH, mode="w") as data_file:
            json.dump(data, data_file, indent=4)
    # Clear userinput interface
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
    website_entry.focus()
    return


# ---------------------------- UI SETUP ------------------------------- #
# Create and open GUI window
app_window = tkinter.Tk()
app_window.title("Password Manager")
app_window.minsize(width=550, height=400)
app_window.config(padx=20, pady=20)

# Logo
app_logo = tkinter.PhotoImage(file="logo.png")
logo_canvas = tkinter.Canvas(width=250, height=200, highlightthickness=0)
logo_canvas.create_image(130, 100, image=app_logo)
logo_canvas.grid(row=1, column=2)

# Labels
website_label = tkinter.Label(text="Website: ", font=LABEL_FONT)
website_label.grid(row=2, column=1)
username_label = tkinter.Label(text="Email/Username: ", font=LABEL_FONT)
username_label.grid(row=3, column=1)
password_label = tkinter.Label(text="Password: ", font=LABEL_FONT)
password_label.grid(row=4, column=1)

# Website Entry
website_entry = tkinter.Entry(width=42, font=ENTRY_FONT)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2, sticky="W", pady=2)

# Username/Email Entry
username_entry = tkinter.Entry(width=42, font=ENTRY_FONT)
username_entry.grid(row=3, column=2, columnspan=2, sticky="W", pady=2)

# Password Entry
password_entry = tkinter.Entry(width=28, font=ENTRY_FONT)
password_entry.grid(row=4, column=2, sticky="W", pady=2)

# "Generate Password" button
generatepassword_button = tkinter.Button(text="Generate Password", font=BUTTON_FONT, command=generate_password)
generatepassword_button.grid(row=4, column=3)

# "Add" button
addpassword_button = tkinter.Button(text="Add", width=36, font=BUTTON_FONT, command=addpassword_button_click)
addpassword_button.grid(row=5, column=2, columnspan=2, sticky="W", pady=20)

# Exit GUI window
app_window.mainloop()
