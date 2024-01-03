from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_passsword.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_username.get()
    password = entry_passsword.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            with open("day_29_password_manager/day_29/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_passsword.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="day_29_password_manager/day_29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:", bg="white")
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username:", bg="white")
label_username.grid(column=0, row=2)

label_password = Label(text="Password:", bg="white")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=54)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")
entry_website.focus()

entry_username = Entry(width=54)
entry_username.grid(column=1, row=2, columnspan=2, sticky="w")
entry_username.insert(0, "me@gmail.com")

entry_passsword = Entry(width=33)
entry_passsword.grid(column=1, row=3, sticky="w")

# Buttons
button_generate = Button(
    text="Generate Password", width=16, highlightthickness=0, command=generate_password
)
button_generate.grid(column=2, row=3, sticky="w")

button_add = Button(text="Add", width=45, highlightthickness=0, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()
