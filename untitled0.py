from tkinter import *
import re
import tkinter.messagebox as messagebox
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfile 
from colorama import Fore, Style
import time
import datetime as dt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
a=Tk()
a.title('Hospital Data Analysis')
a.iconbitmap('Data_stuff.ico')
width=610
height=490
a.minsize(600,413)
screenwidth = a.winfo_screenwidth()
screenheight = a.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
a.geometry(alignstr)
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="orange3")
s.map("TNotebook", background= [("selected", "orange3")])
img=ImageTk.PhotoImage(Image.open('poster.jpg'))
label=Label(a,image=img,bg='purple',anchor=CENTER)
label.pack()
tabcontrol=ttk.Notebook(a)
tabcontrol.pack(expand=1,fill=BOTH)
tab1 = Frame(tabcontrol, background="yellow" ) 
tabcontrol.add(tab1,text='Data Entry')
mainframe1=Frame(tab1)
mainframe1.pack(fill=BOTH,expand=1)
mycan1=Canvas(mainframe1)
mycan1.pack(side=LEFT,fill=BOTH,expand=1)
scroll=ttk.Scrollbar(mainframe1,orient=VERTICAL,command=mycan1.yview)
scroll.pack(side=RIGHT,fill=Y)
mycan1.configure(yscrollcommand=scroll.set)
mycan1.bind('<Configure>',lambda e: mycan1.configure(scrollregion=mycan1.bbox('all')))
secondframe=Frame(mycan1)
mycan1.create_window((1,1),window=secondframe, anchor='nw')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
def importcsv():
    if chk.get()==0:
        messagebox.showwarning('Warning','Please click on the check box')
    else:
        if var.get()=='':
            messagebox.showerror('Error','Some important boxes are empty')
        else:
            k=[var.get(),var1.get(),var2.get(),var3.get(),var4.get(),cal1.get_date(),inp.get(),inp1.get(),inp2.get(),inp3.get(),inp4.get(),inp5.get(),inp6.get()]
            flag=1
            for i in range(7):
                if k[i+6]=='':
                    k[i+6]=0
                    
                elif k[i+6].isdigit():
                    k[i+6]=int(k[i+6])
                else:
                    flag=0
                    messagebox.showerror('Error','Some inputs are invalid')
                    break
            if flag:
                with open('CSVFILE.csv', 'a', newline='') as f_object:
                    writer_object = csv.writer(f_object)
                    writer_object.writerow(k)
                    f_object.close()
                messagebox.showinfo('Success','Data is updated')
lbl=Label(secondframe,bg='yellow',text='')
lbl.pack(ipadx=1000,ipady=400,side="left", expand=True, fill="both")
lbl=Label(secondframe,text='Hospital Name', bg='blue', fg='white', font =("comicsansms 13 bold"))
lbl.place(x=0,y=10)
var=StringVar()
ent= Entry(secondframe,bg='sky blue',bd=4 ,textvariable=var ,relief=SUNKEN,font="Century 10")
ent.place(x=130,y=10)
lbl=Label(secondframe,text='City',bg='#00ffff')
lbl.place(x=10,y=45)
var1=StringVar()
ent= Entry(secondframe,textvariable=var1,width=15)
ent.place(x=10,y=65)
lbl=Label(secondframe,text='District',bg='#00ffff')
lbl.place(x=110,y=45)
var2=StringVar()
ent= Entry(secondframe,textvariable=var2,width=15)
ent.place(x=110,y=65)
lbl=Label(secondframe,text='State',bg='#00ffff')
lbl.place(x=210,y=45)
var3=StringVar()
ent= Entry(secondframe,textvariable=var3,width=15)
ent.place(x=210,y=65)
font1=('Times',8)
coun=pd.read_csv('countries.csv')
my_list=coun['Countries'].tolist()
lbl=Label(secondframe,text='Country',bg='#00ffff')
lbl.place(x=310,y=45)
def my_upd(secondframeidget):
    secondframe = secondframeidget.widget
    inde = int(secondframe.curselection()[0])
    valu = secondframe.get(inde)
    var4.set(valu) 
    l1.delete(0,END)
def my_down(secondframeidget):
    l1.focus()
    l1.selection_set(0)
var4=StringVar()
def get_data(*args):
    search_str=enti.get()
    l1.delete(0,END)
    for element in my_list:
        if(re.match(search_str,element,re.IGNORECASE)):
            l1.insert(END,element)
var4.trace('w',get_data)
enti= Entry(secondframe,textvariable=var4,width=15)
enti.place(x=310,y=65)
l1 = Listbox(secondframe,height=3,font=font1,relief='flat',bg='yellow',highlightcolor= 'SystemButtonFace',width=15)
l1.place(x=310,y=85)
enti.bind('<Down>', my_down)
l1.bind('<Button-1>', my_upd)

lbl=Label(secondframe,text='Date', bg='orange', fg='white')
lbl.place(x=10,y=110)
var5=StringVar()
cal1=DateEntry(secondframe,selectmode='day',bg='yellow')
cal1.place(x=50,y=110)

lbl=Label(secondframe,text='Patients',bg='pink')
lbl.place(x=10,y=140)
inp=StringVar()
ent= Entry(secondframe,textvariable=inp,width=10)
ent.place(x=10,y=160)
lbl=Label(secondframe,text='Beds',bg='pink')
lbl.place(x=90,y=140)
inp1=StringVar()
ent= Entry(secondframe,textvariable=inp1,width=10)
ent.place(x=90,y=160)
lbl=Label(secondframe,text='Deaths',bg='pink')
lbl.place(x=170,y=140)
inp2=StringVar()
ent= Entry(secondframe,textvariable=inp2,width=10)
ent.place(x=170,y=160)
lbl=Label(secondframe,text='Cancer',bg='pink')
lbl.place(x=250,y=140)
inp3=StringVar()
ent= Entry(secondframe,textvariable=inp3,width=10)
ent.place(x=250,y=160)
lbl=Label(secondframe,text='Tuberculosis',bg='pink')
lbl.place(x=330,y=140)
inp4=StringVar()
ent= Entry(secondframe,textvariable=inp4,width=10)
ent.place(x=330,y=160)
lbl=Label(secondframe,text='Accidents',bg='pink')
lbl.place(x=410,y=140)
inp5=StringVar()
ent= Entry(secondframe,textvariable=inp5,width=10)
ent.place(x=410,y=160)
lbl=Label(secondframe,text='Pneumonia',bg='pink')
lbl.place(x=490,y=140)
inp6=StringVar()
ent= Entry(secondframe,textvariable=inp6,width=10)
ent.place(x=490,y=160)
chk=IntVar()
lbl=Label(secondframe,text='Covid',bg='pink')
lbl.place(x=570,y=140)
inp6=StringVar()
ent= Entry(secondframe,textvariable=inp6,width=10)
ent.place(x=570,y=160)
chk=IntVar()
chkbox=Checkbutton(secondframe,text='All entries are correct and ready to submit' ,variable=chk)
chkbox.place(x=10,y=200)
btn=Button(secondframe,bg='brown',text='Submit',command=importcsv )
btn.place(x=10,y=230)

l=[]
def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Csv Files', '*csv')])
    if file_path is not None:
        x=list(csv.reader(file_path))
        while(len(l)>0):
            l.pop()
        l.append(x)
def uploadFiles():
    if len(l)==0:
        messagebox.showwarning('Warning','Please Choose some file')
    else:
        pb1 = ttk.Progressbar(secondframe, orient=HORIZONTAL, length=300, mode='determinate')
        pb1.place(x=40,y=360)
        print(l[-1])
        with open('CSVFILE.csv', 'a', newline='') as f_object:
            writer_object = csv.writer(f_object)
            for i in range(1,len(l[-1])):
                writer_object.writerow(l[-1][i])
            f_object.close()
        l.pop()
        for i in range(5):
            secondframe.update_idletasks()
            pb1['value'] += 30
            time.sleep(0.5)
        pb1.destroy()
        Label(secondframe, text='File Uploaded Successfully!', foreground='green').place(x=40,y=360)
msbtn = Button(secondframe, text ='Select File', command = lambda:open_file(),bg='magenta') 
msbtn.place(x=40,y=290)
upld = Button(secondframe, text='Upload Files', command=uploadFiles ,bg='magenta')
upld.place(x=40,y=320)

tab2 = Frame(tabcontrol, background="yellow" ) 
tabcontrol.add(tab2,text='Data Analysis')
mainframe=Frame(tab2)
mainframe.pack(fill=BOTH,expand=1)
mycan=Canvas(mainframe)
mycan.pack(side=LEFT,fill=BOTH,expand=1)
scroll=ttk.Scrollbar(mainframe,orient=VERTICAL,command=mycan.yview)
scroll.pack(side=RIGHT,fill=Y)
mycan.configure(yscrollcommand=scroll.set)
mycan.bind('<Configure>',lambda e: mycan.configure(scrollregion=mycan.bbox('all')))
def _on_mousewheel1(e,*arg):
    if(tabcontrol.index('current')==1):
        mycan.yview_scroll(-1*(e.delta//120), "units")
    elif(tabcontrol.index('current')==0):
        mycan1.yview_scroll(-1*(e.delta//120), "units")
mycan.bind_all('<MouseWheel>', _on_mousewheel1)
secondframe1=Frame(mycan)
mycan.create_window((1,1),window=secondframe1, anchor='nw')
lbl=Label(secondframe1,bg='yellow',text='')
lbl.pack(ipadx=1000,ipady=400,side="left", expand=True, fill="both")
x=pd.read_csv('CSVFILE.csv')
x['Date'] = [dt.datetime.strptime(d,'%d-%m-%Y').date() for d in x['Date']]
lbl=Label(secondframe1,text='Region Type', bg='orange', fg='white', font =("comicsansms 12 bold"))
lbl.place(x=5,y=10)
mylist1=list(x.head())[1:5]
mylist2=[]
def my_upd1(secondframe1idget):
    secondframe1 = secondframe1idget.widget
    index = int(secondframe1.curselection()[0])
    value = secondframe1.get(index)
    vari.set(value) 
    l2.delete(0,END)
    global mylist2
    mylist2=list(set(x[vari.get()]))
def my_down1(secondframe1idget):
    l2.focus()
    l2.selection_set(0)
vari=StringVar()
def get_data1(*args):
    search_str=ent2.get()
    l2.delete(0,END)
    for element in mylist1:
        if(re.match(search_str,element,re.IGNORECASE)):
            l2.insert(END,element)
vari.trace('w',get_data1)
ent2= Entry(secondframe1,bg='#FFFAF0',bd=4 ,textvariable=vari ,relief=RIDGE,font="Century 9")
ent2.place(x=130,y=10)
l2 = Listbox(secondframe1,height=3,font=font1,relief='flat',bg='yellow',highlightcolor= 'SystemButtonFace',width=15)
l2.place(x=130,y=35)
ent2.bind('<Down>', my_down1)
l2.bind('<Button-1>', my_upd1)
lbl=Label(secondframe1,text='Region', bg='orange', fg='white', font =("comicsansms 12 bold"))
lbl.place(x=5,y=110)

def my_upd2(secondframe2idget):
    secondframe2 = secondframe2idget.widget
    index1 = int(secondframe2.curselection()[0])
    value1 = secondframe2.get(index1)
    vari1.set(value1)
    l3.delete(0,END)
    global k
    k=x[x[vari.get()]==vari1.get()] 
def my_down2(secondframe2idget):
    l3.focus()
    l3.selection_set(0)
vari1=StringVar()
def get_data2(*args):
    search_str=ent3.get()
    l3.delete(0,END)
    for element in mylist2:
        if(re.match(search_str,element,re.IGNORECASE)):
            l3.insert(END,element)
vari1.trace('w',get_data2)
ent3= Entry(secondframe1,bg='#FFFAF0',bd=4 ,textvariable=vari1 ,relief=RIDGE,font="Century 9")
ent3.place(x=130,y=110)
l3 = Listbox(secondframe1,height=3,font=font1,relief='flat',bg='yellow',highlightcolor= 'SystemButtonFace',width=15)
l3.place(x=130,y=135)
ent3.bind('<Down>', my_down2)
l3.bind('<Button-1>', my_upd2)
lbl=Label(secondframe1,text='Parameter', bg='orange', fg='white', font =("comicsansms 12 bold"))
lbl.place(x=5,y=200)
mylist3=list(x.head())[6::]
def my_upd3(secondframe3idget):
    secondframe3 = secondframe3idget.widget
    index2 = int(secondframe3.curselection()[0])
    value2 = secondframe3.get(index2)
    vari2.set(value2) 
    l4.delete(0,END)
def my_down3(secondframe1idget):
    l4.focus()
    l4.selection_set(0)
vari2=StringVar()
def get_data3(*args):
    search_str=ent4.get()
    l4.delete(0,END)
    for element in mylist3:
        if(re.match(search_str,element,re.IGNORECASE)):
            l4.insert(END,element)
vari2.trace('w',get_data3)
ent4= Entry(secondframe1,bg='#FFFAF0',bd=4 ,textvariable=vari2 ,relief=RIDGE)
ent4.place(x=130,y=200)
l4 = Listbox(secondframe1,height=3,font=font1,relief='flat',bg='yellow',highlightcolor= 'SystemButtonFace',width=15)
l4.place(x=130,y=225)
ent4.bind('<Down>', my_down3)
l4.bind('<Button-1>', my_upd3)

ptype = [
	"Line",
	"Bar",
	"Scatter",
	"Stem",
	"Step",
]
def pchoose(*arg):
    pfin=clicked.get()
    fig = Figure(figsize = (10, 4),dpi = 100)
    plot1 = fig.add_subplot(111)
    hname=list(set(k['Hospital Name'].tolist()))
    if (pfin=="Bar"):
        for i in range(len(hname)):
            m=k[k['Hospital Name']==hname[i]]
            plot1.bar(m['Date'],m[vari2.get()],label=hname[i])
    elif(pfin=="Scatter"):
        for i in range(len(hname)):
            m=k[k['Hospital Name']==hname[i]]
            plot1.scatter(m['Date'],m[vari2.get()],label=hname[i])
    elif(pfin=="Stem"):
        for i in range(len(hname)):
            m=k[k['Hospital Name']==hname[i]]
            plot1.stem(m['Date'],m[vari2.get()],label=hname[i])
    elif(pfin=="Step"):
        for i in range(len(hname)):
            m=k[k['Hospital Name']==hname[i]]
            plot1.step(m['Date'],m[vari2.get()],label=hname[i])
    else:
        for i in range(len(hname)):
            m=k[k['Hospital Name']==hname[i]]
            plot1.plot(m['Date'],m[vari2.get()],label=hname[i])
    plot1.set_title(vari2.get())
    plot1.set_xlabel('Date')
    plot1.legend()
    canvas = FigureCanvasTkAgg(fig, secondframe1)
    canvas.draw()
    canvas.get_tk_widget().place(x=310,y=50)
    toolbar = NavigationToolbar2Tk(canvas ,secondframe1 )
    toolbar.update()
    toolbar.place(x=1010,y=50)
    canvas.get_tk_widget().place(x=310,y=50)
clicked=StringVar()
clicked.set( "Choose the desired plot type" )
plotchoose=OptionMenu( secondframe1 , clicked ,*ptype)
plotchoose.config(indicatoron=0,height = 2,width = 25,font=('Helvetica', 11))
plotchoose.place(x=750,y=0)
clicked.trace('w',pchoose)
helv10 = ('Helvetica',10)
pmenu = secondframe1.nametowidget(plotchoose.menuname)
pmenu.config(font=helv10)

tab3 = Frame(tabcontrol, background="yellow" )
tabcontrol.add(tab3,text='Notes')
inputtxt = Text(tab3 ,height = 5 ,width = 20 )
inputtxt.pack()
printButton = Button(tab3 ,text = "Print" ,command = printInput )
printButton.pack()
lbl = Label(tab3, text = "")
lbl.pack()

def close():
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        a.destroy()
        val=messagebox.askquestion('Feedback',"Was your experience good \U0000263A")
        if val=='yes':
            msg='Great, Please rate us on Git '
        else:
            msg='Tell us what went wrong at adarshsantoria@gmail.com'
        messagebox.showinfo('Thanks',msg)
a.protocol('WM_DELETE_WINDOW',close)
a.configure(bg='sky blue')
a.mainloop()
