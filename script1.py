from tkinter import *
import backend
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END, row)
def valid_isbn(isbn_var):
        isbn_var = str(isbn_var)
        print(isbn_var)
        if len(isbn_var)!= 10 and len(isbn_var)!= 13:
            return False
        if len(isbn_var) == 10:
            sum1 =0
            count = 1
            idx= len(isbn_var)-1
            while idx>=0:
                sum1+= int(isbn_var[idx])*count
                count+=1
                idx-=1
            if sum1%11 == 0:
                return True
            else:
                print("hey")
                return False
        else:
            sum1 =0
            count = 1
            idx= len(isbn_var)-1
            while idx>=0:
                if count%2==0:
                    sum1+= int(isbn_var[idx])*3
                else:
                    sum1+= int(isbn_var[idx])
                count+=1
                idx-=1

            if sum1%10 == 0:
                return True
            else:
                print(sum1)
                return False







def insert_command():
    if valid_isbn(isbn_text.get()) == True:
        backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END, row)
    else:
        list1.delete(0,END)
        list1.insert(END, "Not a valid isbn!!!")
def get_selected_row(event):
    global selected_tuple
    if len(list1.curselection())<1:
        return
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)
window = Tk()
l1 = Label(window, text="Title")
l1.grid(row=0,column=0)
l2 = Label(window, text="Author")
l2.grid(row=0,column=2)
l3 = Label(window, text="Year")
l3.grid(row=1,column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan = 2)

sb1= Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)
b1 = Button(window, text="View all", width=12, command = view_command)
b1.grid(row= 2, column = 3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row= 3, column = 3)

b3 = Button(window, text="Add Entry", width=12, command=insert_command)
b3.grid(row= 4, column = 3)

b4 = Button(window, text="Update", width=12,command = update_command)
b4.grid(row= 5, column = 3)

b5 = Button(window, text="Delete", width=12, command = delete_command)
b5.grid(row= 6, column = 3)

b6 = Button(window, text="Close", width=12)
b6.grid(row= 7, column = 3)

window.mainloop()
