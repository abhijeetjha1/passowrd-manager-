from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #





# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("My Pass")
window.config(padx=50,pady=50)
canvas = Canvas(height=200,width= 200)
img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_text=Label(text="Website:")
website_text.grid(row=1,column=0)
website_input=Entry(width=45)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)

email_txt=Label(text="email/username:")
email_txt.grid(row=2,column=0)
email_input=Entry(width=45)
email_input.insert(END,"discoverwithabhi@gmail.com")
email_input.grid(row=2,column=1,columnspan=2)

password_text=Label(text="Password:")
password_text.grid(row=3,column=0)
password_input=Entry(width=27)
password_input.grid(row=3,column=1)

gen_butt=Button(text="Generate Password",highlightthickness=0)
gen_butt.grid(row=3,column=2)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def Add():
    w = website_input.get()
    e = email_input.get()
    p = password_input.get()
    if len(w)==0 or len(p)==0 :
        messagebox.showwarning(title="Opps!" ,message="Please don't leave password or website empty")
    else:
        data = f"{w} | {e} | {p} \n"
        with open("data.txt", "a") as dat:
            dat.writelines(data)
        website_input.delete(0,END)
        password_input.delete(0,END)
        messagebox.showinfo(title="Saved",message="your password has been saved")

add_butt=Button(text="Add",width=38,command=Add)
add_butt.grid(row=4,column=1,columnspan=2)



window.mainloop()