
from tkinter import*
from tkinter import StringVar

sys = Tk()
sys.geometry("480x440")
sys.config(bg="#B5D43B")
sys.resizable(width=False,height=False)
sys.title('Simple Email Slicer')



#ALL THE LABELS ARE HERE
greeting = Label(text="Welcome to A Simple Email Slicer!",font=(12),foreground="white",background="#B5D43B")
Info = Label(text="Enter your email id click the done button!\n The application will extract your username and domain name.",foreground= "#434738",background="#B5D43B",font=(10))
entry_label = Label(foreground= "#434738",font=(10),background="#B5D43B",text="Enter Your Email Id: ")
result_label = Label(font=(10),foreground= "#434738",background="#B5D43B",text="The results are as follows:")
empty_label0=Label(background="#B5D43B")
empty_label1=Label(background="#B5D43B")
empty_label2=Label(background="#B5D43B")
empty_label3=Label(background="#B5D43B")
empty_label4=Label(background="#B5D43B")
empty_label5=Label(background="#B5D43B")
 

#EntryBox
e1 = StringVar()
entry = Entry(font=(11),width=50,justify='center', textvariable=e1)


 
#Result box
text_box = Text(height=5,width=50)

#Result
def result():
    try:
        email=entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', END)
        msg = 'Email entered was: {}\nYour email username is {}\nAnd your email domain server is {}'
        msg_formatted = msg.format(email,username,domain)
        text_box.insert(END,msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', END)
        text_box.insert(END,"ERROR!")

def delete():
    text_box.delete('1.0', END)
    entry.delete(0, 'end')

#The two Buttons
button = Button(text="Slicer!",font=(11), command= result)
reset=Button(text="Reset!",font=(11), command=delete)


#place
greeting.pack()
Info.pack()
empty_label0.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()




sys.mainloop()