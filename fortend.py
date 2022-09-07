from tkinter import *
import bakend

def clear_list():
    list_1.delete(0,END)

def fill_book(books):
    for book in books:
        list_1.insert(END, book)


window = Tk()
window.title("Manage Library")

# ====================================Lable========================================
l1 = Label(window,text="title")
l1.grid(row=0,column=0)

l2 = Label(window,text="author")
l2.grid(row=0,column=2)

l3 = Label(window,text="year")
l3.grid(row=1,column=0)

l4 = Label(window,text="isbn")
l4.grid(row=1,column=2)

# ====================================Enrties========================================

title_text = StringVar
e1 = Entry(window,textvariable = "title_text")
e1.grid(row=0,column=1)

author_text = StringVar
e2 = Entry(window,textvariable = "author_text")
e2.grid(row=0,column=3)

year_text = StringVar
e3 = Entry(window,textvariable = "year_text")
e3.grid(row=1,column=1)

isbn_text = StringVar
e4 = Entry(window,textvariable = "isbn_text")
e4.grid(row=1,column=3)

# ====================================list box========================================

list_1 = Listbox(window , width=35 , height=6)
list_1.grid(row=2,column=0,rowspan=6,columnspan=2)

def get_selected_row(event):
    # noinspection PyGlobalUndefined
    global selected_book
    if len(list_1.curselection()) > 0:
        index = list_1.curselection()[0]
        selected_book = list_1.get(index)
    # title
    e1.delete(0,END)
    e1.insert(END,selected_book[1])
    # author
    e2.delete(0, END)
    e2.insert(END, selected_book[2])
    # year
    e3.delete(0, END)
    e3.insert(END, selected_book[3])
    # isbn
    e4.delete(0, END)
    e4.insert(END, selected_book[4])

list_1.bind("<<listboxselect>>",get_selected_row)

# ====================================Scrollbar========================================

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list_1.configure(yscrollcommand=sb1.set)

# ====================================button========================================

def view_command():
    clear_list()
    books = bakend.view()
    fill_book(books)

b1 = Button(window,text="View All",width=12 , command=lambda :view_command())
b1.grid(row=2,column=3)

def search_command():
    clear_list()
    books = bakend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    fill_book(books)

b2 = Button(window,text ="Search Entry",width=12,command=lambda :search_command())
b2.grid(row=3,column=3)

def add_command():
    bakend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

b3 = Button(window,text = "Add Entry" ,width=12 , command = lambda : add_command())
b3.grid(row=4,column=3)

def update_command():
    bakend.update(selected_book[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

b4 = Button(window,text = "Update Selected" ,width=12 ,command=lambda:update_command())
b4.grid(row=5,column=3)


def delete_command():
    bakend.delete(selected_book[0])
    view_command()

b5 = Button(window,text="Delete Selected",width=12, command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()
