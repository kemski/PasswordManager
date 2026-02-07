import random
from tkinter import *
from tkinter import messagebox
import pyperclip

FONT_NAME = "Courier"




# ------------------- LOGIC ----------------- #
def cleaning_user_info_entry(event=None):
    user_info_entry.delete(0, END)

def cleaning_password_entry(event=None):
    password_entry.delete(0, END)


def cleaning_website_entry(event=None):
    website_entry.delete(0, END)

def datas_save():
    domain_address = website_entry.get()
    e_mail_address = user_info_entry.get()
    user_password = password_entry.get()

    data_set = f'{domain_address} | {e_mail_address} | {user_password}'
    if domain_address == "" or e_mail_address == "" or user_password == "":
        messagebox.showerror(title="Błąd", message="Nie uzupełniłeś wszystkich danych")
    elif domain_address != "" or e_mail_address != "" or user_password != "":
        is_ok = messagebox.askokcancel(title=domain_address, message=f"e-mail: {e_mail_address}\n hasło: {user_password}\n Zapisać?")
        if is_ok:
            pyperclip.copy(user_password)
            with open("data.txt", "a") as file:
                file.write(f'{data_set}\n')

    password_entry.delete(0, END)
    user_info_entry.delete(0, END)
    website_entry.delete(0, END)

def password_generator():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"
    all_chars = letters + numbers + symbols

    new_password = ""
    for _ in range(1,13):
        new_password+=random.choice(all_chars)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)



# --- UI SETUP ---
window = Tk()
window.config(height=800, width=600)
window.title("Password Generator")


# --- CONTENT ---
canvas = Canvas( width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(70,95,  image=tomato_img)
canvas.grid(column=1, row=0, padx=20, pady=20)

# ----- Website Label ------ #
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")

# ----- Website Entry -------- #
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.insert(0, "www.example.com")
website_entry.bind("<FocusIn>", cleaning_website_entry)

# ---- Emai/user name Label -------- #
user_info_label = Label(text="Email/Username:")
user_info_label.grid(column=0, row=2, sticky="e", padx=(40, 0))

# ----- Emai/user name Entry -------- #
user_info_entry = Entry(width=35)
user_info_entry.grid(column=1, row=2, columnspan=2, sticky="w")
user_info_entry.insert(0, "example@mail.com")
user_info_entry.bind("<FocusIn>", cleaning_user_info_entry)

# ---- Password Label -------- #
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

# ----- Password Entry -------- #
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")
password_entry.insert(0, "Password..")
password_entry.bind("<FocusIn>", cleaning_password_entry)

# ----- Generate Password Button -------- #
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=1, row=3, sticky="e", columnspan=2, padx=(170,110))

# ------------- ADD Button ----------------- #
add_button = Button(text="ADD", width=32, command=datas_save)
add_button.grid(column=1, row=4, sticky="w", pady=(0, 40), columnspan=3 )


# --- CENTER WINDOW ---
window.update_idletasks()
w = window.winfo_width()
h = window.winfo_height()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
x = (sw - w) // 2
y = (sh - h) // 2
window.geometry(f"{w}x{h}+{x}+{y}")

# --- FOCUS / TOPMOST (macOS + PyCharm) ---
window.lift()
window.attributes("-topmost", True)
window.after(200, lambda: window.attributes("-topmost", False))
window.focus_force()




window.mainloop()
