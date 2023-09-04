from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD FINDER ------------------------------- #


def password_finder():
    try:
        with open("data.json", "r") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="opps", message="No Data File Found In Records")

    else:
        site_name = website_entry.get()
        if len(site_name) != 0:
            try:
                email_of_user = file_data.get(f"{site_name}").get("email")
                password_of_user = file_data.get(f"{site_name}").get("password")

            except AttributeError:
                messagebox.showerror(title="opps", message="No data found for this website")

            else:
                messagebox.showinfo(title=f"{site_name}", message=f"Your Email: {email_of_user}\n Your Password:\n{password_of_user}")
                print(f"{email_of_user},{password_of_user}")

        else:
            messagebox.showerror(title="opps", message="Please Don't Leave place empty")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generater():
    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbol = [random.choice(symbols) for _ in range(random.randint(5, 8))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 5))]

    password_list = password_letter + password_symbol + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    email_data = email_entry.get()
    website_data = website_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="opps", message="Please Don't Leave any place empty")

    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"This is your information: \n Email: {email_data}\n Password: {password_data} \n Is this okay?")
        if is_ok:
            all_data = {website_data:
                {
                    "email": email_data,
                    "password": password_data
                }}
            # print(all_data)
            try:
                with open("data.json", "r") as file:
                    # reading file
                    data = json.load(file)
                # Updating data
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(all_data, file, indent=4)

            else:
                data.update(all_data)
                # writing data
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(400,400)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)



website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "suri@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

add_button = Button(text="Add", width=36, font=(FONT_NAME, 10, "bold"), command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

generated_password_button = Button(text="Generate Password", font=(FONT_NAME, 10, "bold"), width=20 ,command=password_generater)
generated_password_button.grid(column=3, row=3)

search_button = Button(text="Search", width=20, font=(FONT_NAME, 10, "bold"), command=password_finder)
search_button.grid(column=3, row=1)

window.mainloop()
