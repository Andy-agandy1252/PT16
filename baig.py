import tkinter as tk

window = tk.Tk()
#------------informacija------------
from info import *
#------------kodas---------
window.title('Kelioniu gidas')
window.geometry('1300x630')
window.config(bg='#F4EFEA')

#-----------funkcijos----
def newwindow(frame):
    frame.tkraise()

def miestai(frame):
    frame.tkraise()
    listbox.delete(0, END)
    for miestai in city_list:
        listbox.insert(0, miestai)
        listbox.grid(row=2, column=1)

def paminklai(frame):
    frame.tkraise()
    listbox.delete(0, END)
    for vietos in paminklai_visi:
        listbox.insert(0, vietos)
        listbox.grid(row=2, column=1)
        scrollbar = tk.Scale(frame2, from_=0, to=16, orient=VERTICAL)
        scrollbar.config(command=listbox.yview)

def muzejai(frame):
    frame.tkraise()
    listbox.delete(0, END)
    for vietos in muzejai_visi:
        listbox.insert(0, vietos)
        listbox.grid(row=2, column=1)

def kultura(frame):
    frame.tkraise()
    listbox.delete(0, END)
    for vietos in kultura_visi:
        listbox.insert(0, vietos)
        listbox.grid(row=2, column=1)

def aprasymai(event):
    frame2label1.config(image=sarasas_visko[listbox.get(listbox.curselection())][0])
    frame2label2.config(text=sarasas_visko[listbox.get(listbox.curselection())][1])

def miestu_pasirinkimas():
    if listbox.get(listbox.curselection()) == "Vilnius":
        miesto_vietos = vilnius
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Kaunas":
        miesto_vietos = kaunas
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Klaipėda":
        miesto_vietos = klaipeda
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Šiauliai":
        miesto_vietos = siauliai
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Panevėžys":
        miesto_vietos = panevezys
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Alytus":
        miesto_vietos = alytus
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Marijampolė":
        miesto_vietos = marijampole
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Mažeikiai":
        miesto_vietos = mazeikiai
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Jonava":
        miesto_vietos = jonava
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Utena":
        miesto_vietos = utena
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Kėdainiai":
        miesto_vietos = kedainiai
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Tauragė":
        miesto_vietos = taurage
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Telšiai":
        miesto_vietos = telsiai
        return miesto_vietos
    elif listbox.get(listbox.curselection()) == "Ukmergė":
        miesto_vietos = ukmerge
        return miesto_vietos

def miestai2(frame):
    frame.tkraise()
    listbox.delete(0, END)
    for miestai in city_list:
        listbox.insert(0, miestai)
        listbox.grid(row=2, column=1)
        frame2button1 = tk.Button(frame2, text='     Pasirinkti     ', command=lambda: miestu_window(frame2))
        frame2button1.grid(row=3, column=1)

def miestu_window(frame):
    frame.tkraise()
    miesto_vietos = miestu_pasirinkimas()

    if listbox.get(listbox.curselection()) == listbox.get(listbox.curselection()):
        listbox.delete(0, END)
        frame2button1 = tk.Button(frame2, text='Grizti i miestus', command=lambda: miestai2(frame2), bg='#F4EFEA')
        frame2button1.grid(row=3, column=1)
        for vietos in miesto_vietos:
            listbox.insert(END, vietos)
            listbox.grid(row=2, column=1)
#----------Freimai--------------
frame1 = tk.Frame(window, bg='#F4EFEA')
frame2 = tk.Frame(window, bg='#F4EFEA')
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky='news')

#-----------------first Page-----
frametitle = tk.Label(frame1, text='Atraskite Lietuvą iš naujo',
                       font=('Areal', 30, 'bold'),
                       bg='#F4EFEA', padx=200)
framelable = tk.Label(frame1, text='I kurį miestą noretumėte vykti',
                      font=('Areal', 20, 'bold'),
                      bg='#F4EFEA')
framebutton1 = tk.Button(frame1, text='Miestų sąrašas',
                         image=miestusaraso_foto,
                         compound='bottom',
                         font=('Areal', 20),
                         command=lambda: miestai(frame2),
                         bg='#F4EFEA')
framebutton2 = tk.Button(frame1, text='Paminklai',
                         image=paminklu_foto,
                         compound='bottom',
                         command=lambda: paminklai(frame2),
                         bg='#F4EFEA')
framebutton3 = tk.Button(frame1, text='Muziejai',
                         image=muzieju_foto,
                         compound='bottom',
                         command=lambda: muzejai(frame2),
                         bg='#F4EFEA')
framebutton4 = tk.Button(frame1, text='Kultūros paveldai',
                         image=kulturos_foto,
                         compound='bottom',
                         command=lambda: kultura(frame2),
                         bg='#F4EFEA')
#--------------second Page------------
frame2button_atgalipradzia = tk.Button(frame2, text='Pradzia',command=lambda: newwindow(frame1),bg='#F4EFEA')
frame2button_atgalmiesta = tk.Button(frame2, text='I Miestus',command=lambda: miestai2(frame2),bg='#F4EFEA')
listbox = tk.Listbox(frame2, bg='#F4EFEA',font='TimesNewRoman',width=46, height=30)
frame2button1 = tk.Button(frame2, text='Pasirinkti',command=lambda: miestu_window(frame2), bg='#F4EFEA')
frame2label1 = tk.Label(frame2, image='',bg='#F4EFEA')
frame2label2 = tk.Label(frame2, text='',font='TimesNewRoman',bg='#F4EFEA')
window.bind("<<ListboxSelect>>", aprasymai)

#===============migtuku isdestimas-------
#---------------1page-----
frametitle.grid(row=1, column=2)
framelable.grid(row=2, column=2)
framebutton1.grid(row=3, column=2)
framebutton2.grid(row=4, column=1)
framebutton3.grid(row=4, column=2)
framebutton4.grid(row=4, column=3)
#---------------2page-----
frame2button_atgalipradzia.grid(row=1, column=1)
frame2button_atgalmiesta.grid(row=1, column=2)
listbox.grid(row=2, column=1)
frame2button1.grid(row=3, column=1)
frame2label1.grid(row=2, column=4)
frame2label2.grid(row=2, column=5)

newwindow(frame1)
window.mainloop()