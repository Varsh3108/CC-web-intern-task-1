from tkinter import *
import tkinter.font
from tkinter import ttk #tinker.ttk is a widget used to style tinker elements whereas tinker elements are used to style buttons,labels,etc.
from googletrans import Translator,LANGUAGES

window=Tk()      #graphical interaction
window.title("Live language translator")
window.geometry("1100x500")
window.resizable(0,0)
p1=PhotoImage(file='globe.png')
window.iconphoto(False,p1)
window['background']='#F0F8FF'

Label(window,text="Language Translator",font="TimesNewRomanGreek 20").pack()


#Creating space for entering the text u wanna change
Label(window,text="Enter Text",font="TimesNewRoman 13 bold",bg="LightBlue").place(x=165, y=90)


Input_text=Entry(window,font="TimesNewRoman 12",width=50)
Input_text.place(x=50,y = 130)
Input_text.get()


#Creating space for the output text
Label(window,text="Output",font="TimesNewRoman 14 bold",bg="LightBlue").place(x=800,y=90)
Output_text=Text(window,font="TimesNewRoman 12",height=5,padx=10,pady=10,width=50)
Output_text.place(x=600,y=130)


#Creating a button for choosing language
language=list(LANGUAGES.values())


dest_lang=ttk.Combobox(window,values=language,width=22)
dest_lang.place(x=130,y=160)
dest_lang.set('Choose language')

def Translate():
    translator=Translator()
    translated=translator.translate(text=Input_text.get(),dest=dest_lang.get())
    Output_text.insert(1.0,END)
    Output_text.insert(END,translated.text)

trans_btn=Button(window,text='Click here to translate!',font="TimesNewRoman 12 bold",pady=5,command=Translate,bg='#474973',activebackground='#a69cac')
trans_btn.place(x=450,y=300)


window.mainloop()



