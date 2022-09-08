from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("450x250")
root.resizable(False,False)
root.title("The West Application Form")
def register():
    name =namevalue.get()
    phone =phonevalue.get()
    age =agevalue.get()
    email =emailvalue.get()

    # if else condition
    if name=="":
        messagebox.showerror("       Missing:name        ")
    elif phone=="":
        messagebox.showerror("       Missing:number      ")
    elif age=="":
        messagebox.showerror("       Missing:age         ")
    elif email=="":
        messagebox.showerror("       Missing:email       ")
    else:
        Label(root,text="Registration Successful",font="12",fg="green").grid(row= 12,column=3)

    with open(name+"txt","w")as f:
        f.write("name: "+name+"\n")
        f.write("age: "+age+"\n")
        f.write("phone: "+phone+"\n")
        f.write("email: "+email+"\n")

def clear():
    nameentry.delete(0,END)
    ageentry.delete(0,END)
    phoneentry.delete(0,END)
    emailentry.delete(0,END)



#Heading
Label(root,text="The West Association Application Form",font="ar 15 bold").grid(row=0,column=3)

# Field Name
name = Label(root,text="Name")
phone = Label(root,text="Phone")
age = Label(root,text="Age")
email = Label(root,text="Email ID")
#Packing Entry Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
age.grid(row=3,column=2)
email.grid(row=4,column=2)

namevalue = StringVar()
phonevalue = StringVar()
agevalue = StringVar()
emailvalue = StringVar()
checkvalue = IntVar()

#Creating Entry Field
nameentry = Entry(root, textvariable=namevalue )
phoneentry = Entry(root, textvariable =phonevalue)
ageentry = Entry(root, textvariable =agevalue)
emailentry = Entry(root, textvariable =emailvalue)


#Packing Entry Field
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
ageentry.grid(row=3,column=3)
emailentry.grid(row=4,column=3)


#Creating Checkbox
checkbtn = Checkbutton(text ="Remember Me?",variable =checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="Register",command=register).grid(row=7,column=3)
Button(text="Clear",command=clear).grid(row= 10,column=3)


root.mainloop()

