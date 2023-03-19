from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from tkinter.ttk import *
from PIL import Image,ImageTk


# ----------------------------SEARCHING PASSWORDS -------------------------------#Jsp3V\>a5@EqI0Js
def search_password():
    website = entry_web.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR!!", message="No Data File Exist")
    else:
        if website in data:
            exact_data = data[website]
            messagebox.showinfo(title=f"Your Password for {website}",
                            message=f"Email:{exact_data['email']}\nPassword:{exact_data['password']}")
        else:
            messagebox.showinfo(title="ERROR!!", message="No Such Web Site Has Been Saved")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    alphabets = alpha.split(",")
    cha = "!,@,#,$,%,^,&,*,(,),{,},|,:,<,>,?,/,;,',[,],\,-"
    characters = cha.split(",")
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    pass_alpha = [random.choice(alphabets) for _ in range(6)]
    pass_char = [random.choice(characters) for _ in range(4)]
    pass_num = [random.choice(digits) for _ in range(2)]
    passed = pass_num + pass_char + pass_alpha
    random.shuffle(passed)
    password = "".join(passed)
    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    email = entry_user.get()
    password = entry_pass.get()
    website = entry_web.get()
    new_dict = {website: {
        "email": email,
        "password": password
    }}
    if email == "" or password == "" or website == "":
        messagebox.showerror(title="Error!!", message="fill all the boxes to proceed")
    else:
        is_ok = messagebox.askokcancel(title="Save password", message="Is it ok to save the 'Password'")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_dict, file, indent=4)
            else:
                data.update(new_dict)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=42)
            finally:
                entry_web.delete(0, END)
                entry_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = ImageTk.PhotoImage(Image.open("C:/Users/gunde/Desktop/python/img222.jpg"))
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3)
entry_web = Entry(width=25)
entry_web.focus()
entry_web.grid(row=1, column=1, columnspan=1)
entry_user = Entry(width=43)
entry_user.insert(0, "ravitejagundeti13@gmail.com")
entry_user.grid(row=2, column=1, columnspan=2)
entry_pass = Entry(width=25)
entry_pass.grid(column=1, row=3)
button_gen = Button(width=20, text="Generate Password", command=pass_generator)
button_gen.grid(column=2, row=3)
button_add = Button(width=35, text="Add", command=add_pass)
button_add.grid(column=1, row=4, columnspan=2)
button_search = Button(text="Search", command=search_password)
button_search.grid(column=2, row=1)
window.mainloop()
