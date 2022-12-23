from tkinter import *
import db_p3_lr_update
import db_p3_lr_predict_customer


def initializeOpe():
    import db_p3_lr

def updateCSV():
    addr = get_csv()
    db_p3_lr_update.update(addr)
    csv_addr.delete(0, END)

def getQuote():
    possibility = str(10000 * db_p3_lr_predict_customer.predictCustomer(get_one(), get_two(), get_three(), get_four(), get_five(), get_six(), get_seven(), get_eight()) + 9000)
    for item in one, two, three, four, five, six, seven, eight:
        item.delete(0, END)
    label.configure(text=possibility)


# this is a function to get the user input from the text input box
def get_csv():
    userInput = csv_addr.get()
    return userInput


# this is a function to get the user input from the text input box
def get_one():
    one_value = float(one.get())
    return one_value


# this is a function to get the user input from the text input box
def get_two():
    userInput = float(two.get())
    return userInput


# this is a function to get the user input from the text input box
def get_three():
    userInput = float(three.get())
    return userInput


# this is a function to get the user input from the text input box
def get_four():
    userInput = float(four.get())
    return userInput


# this is a function to get the user input from the text input box
def get_five():
    userInput = float(five.get())
    return userInput


# this is a function to get the user input from the text input box
def get_six():
    userInput = float(six.get())
    return userInput


# this is a function to get the user input from the text input box
def get_seven():
    userInput = float(seven.get())
    return userInput


# this is a function to get the user input from the text input box
def get_eight():
    userInput = float(eight.get())
    return userInput


root = Tk()

# This is the section of code which creates the main window
root.geometry('889x586')
root.configure(background='#F0F8FF')
root.title('Insurance Quote System')

# This is the section of code which creates a label
Label(root, text='CSV Address', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=34)

# This is the section of code which creates a text input box
csv_addr = Entry(root)
csv_addr.place(x=42, y=61)

# This is the section of code which creates a label
Label(root, text='Customer Info', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=48, y=156)

# This is the section of code which creates a button
Button(root, text='Enter', bg='#F0F8FF', font=('arial', 12, 'normal'), command=updateCSV).place(x=200, y=53)

# This is the section of code which creates a text input box
Label(root, text='Pregnancies: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=200)
one = Entry(root)
one.place(x=175, y=200)

# This is the section of code which creates a text input box
Label(root, text='Glucose: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=235)
two = Entry(root)
two.place(x=175, y=235)

# This is the section of code which creates a text input box
Label(root, text='Blood Pressure: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=270)
three = Entry(root)
three.place(x=175, y=270)

# This is the section of code which creates a text input box
Label(root, text='Skin Thickness: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=305)
four = Entry(root)
four.place(x=175, y=305)

# This is the section of code which creates a text input box
Label(root, text='Insulin: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=340)
five = Entry(root)
five.place(x=175, y=340)

# This is the section of code which creates a text input box
Label(root, text='BMI: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=375)
six = Entry(root)
six.place(x=175, y=375)

# This is the section of code which creates a text input box
Label(root, text='Diabetes Func: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=410)
seven = Entry(root)
seven.place(x=175, y=410)

# This is the section of code which creates a text input box
Label(root, text='Age: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=45, y=445)
eight = Entry(root)
eight.place(x=175, y=445)

# This is the section of code which creates a button
Button(root, text='Confirm', bg='#F0F8FF', font=('arial', 12, 'normal'), command=getQuote).place(x=140, y=490)
Button(root, text='Initialize', bg='#F0F8FF', font=('arial', 12, 'normal'), command=initializeOpe).place(x=445, y=34)

# This is the section of code which creates the label
label = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
label.place(x=490, y=180)
Label(root, text='Quote: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=445, y=134)

root.mainloop()
