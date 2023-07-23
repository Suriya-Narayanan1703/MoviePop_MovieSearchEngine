import pandas as pd
import numpy as np
import tkinter as tk
#import customtkinter as ctk
import ast

list_1=pd.read_csv("movies.csv")
ll=pd.DataFrame(list_1,columns=["original_title","budget","genres","overview","release_date","revenue","runtime","vote_average"])
list_2=pd.read_csv("credits.csv")
#print(list_2)
ll_2=pd.DataFrame(list_2,columns=["title","cast","crew"])
#llo=len(ll["original_title"])
#a="Avatar"
#print(ll["original_title"][0])
#for i in range(0,llo):
 #   if(a==ll["original_title"][i]):
  #      print("found")



#print(ll["original_title"][6])

def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

ll['genres']=ll['genres'].apply(convert)
ll_2['cast']=ll_2['cast'].apply(convert)
ll_2['crew']=ll_2['crew'].apply(convert)


##gui

def play():
    n=name_var.get()
    llo=len(ll["original_title"])
    for i in range(0,llo):
       if((n.capitalize())==ll["original_title"][i] or n in ll["original_title"][i]):
           label1 = tk.Label(app, text=("Title:",ll["original_title"][i])).place(x=150, y=140)
           label2 = tk.Label(app, text=("Budget:", ll["budget"][i])).place(x=100, y=160)
           label3 = tk.Label(app, text=("Genre:", ll["genres"][i])).place(x=100, y=180)
           label4 = tk.Label(app, text=("Release Date:", ll["release_date"][i])).place(x=100, y=200)
           label5 = tk.Label(app, text=("Revenue:", ll["revenue"][i])).place(x=100, y=220)
           label6 = tk.Label(app, text=("Runtime:", ll["runtime"][i])).place(x=100, y=240)
           label7 = tk.Label(app, text=("Votes:", ll["vote_average"][i])).place(x=100, y=260)
           ll_dip1=ll["overview"][i]
           m=int(len(ll_dip1)/2)
           ll_dip11 = ll_dip1[0:m]
           ll_dip12 = ll_dip1[m:]
           label8 = tk.Label(app, text=("Overview:", ll_dip11)).place(x=100, y=280)
           label8 = tk.Label(app, text=("-",ll_dip12)).place(x=100, y=300)
           #label1 = tk.Label(app, text=("Title:", n.capitalize())).place(x=100, y=160)


def show():
    m=clicked.get()
    q=str(m)
    #print(m)
    label = tk.Label(app, text=(m,"Movies")).place(x=470,y=110)
    #label.config(text=).place()
    sp_1 = ll['genres']
    sp_1c = len(sp_1)

    sp_2 = []

    for i in range(0, sp_1c):
        m = sp_1[i]
        sp_1m = len(m)
        for j in range(0, sp_1m):
            sp_r = m[j]
            if (sp_r not in sp_2):
                sp_2.append(sp_r)
            else:
                pass

    mov_lis1 = []
    for i in range(0, sp_1c):
        mov1 = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Action" in sp_1[i]):
                mov_lis1.append(ll["original_title"][i])
    mov_l1 = [*set(mov_lis1)]

    mov_lis2 = []
    for i in range(0, sp_1c):
        mov2 = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Adventure" in sp_1[i]):
                mov_lis2.append(ll["original_title"][i])
    mov_l2 = [*set(mov_lis2)]

    mov_lis3 = []
    for i in range(0, sp_1c):
        mov3 = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Fantasy" in sp_1[i]):
                mov_lis3.append(ll["original_title"][i])
    mov_l3 = [*set(mov_lis3)]

    mov_lis4 = []
    for i in range(0, sp_1c):
        mov4 = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Science Fiction" in sp_1[i]):
                mov_lis1.append(ll["original_title"][i])
    mov_l4 = [*set(mov_lis4)]

    mov_lis5 = []
    #print(mov_l1)
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Crime" in sp_1[i]):
                mov_lis5.append(ll["original_title"][i])
    mov_l5 = [*set(mov_lis5)]

    mov_lis6 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Drama" in sp_1[i]):
                mov_lis6.append(ll["original_title"][i])
    mov_l6 = [*set(mov_lis6)]

    mov_lis7 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Thriller" in sp_1[i]):
                mov_lis7.append(ll["original_title"][i])
    mov_l7 = [*set(mov_lis7)]

    mov_lis8 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Animation" in sp_1[i]):
                mov_lis1.append(ll["original_title"][i])
    mov_l8 = [*set(mov_lis8)]

    mov_lis9 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Family" in sp_1[i]):
                mov_lis9.append(ll["original_title"][i])
    mov_l9 = [*set(mov_lis9)]

    mov_lis10 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Comedy" in sp_1[i]):
                mov_lis10.append(ll["original_title"][i])
    mov_l10 = [*set(mov_lis10)]

    mov_lis11 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Romance" in sp_1[i]):
                mov_lis11.append(ll["original_title"][i])
    mov_l11 = [*set(mov_lis11)]

    mov_lis12 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Horror" in sp_1[i]):
                mov_lis12.append(ll["original_title"][i])
    mov_l12 = [*set(mov_lis12)]

    mov_lis13 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("History" in sp_1[i]):
                mov_lis13.append(ll["original_title"][i])
    mov_l13 = [*set(mov_lis13)]

    mov_lis14 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("War" in sp_1[i]):
                mov_lis14.append(ll["original_title"][i])
    mov_l14 = [*set(mov_lis14)]

    mov_lis15 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Music" in sp_1[i]):
                mov_lis15.append(ll["original_title"][i])
    mov_l15 = [*set(mov_lis15)]

    mov_lis16 = []
    for i in range(0, sp_1c):
        mov = sp_1[i]
        for j in range(0, len(sp_2)):
            if ("Documentary" in sp_1[i]):
                mov_lis16.append(ll["original_title"][i])
    mov_l16 = [*set(mov_lis16)]



    X=472
    Y=132
    if(q == "Action"):
        for o in range(0,5):
            label = tk.Label(app, text=(o+1,mov_l1[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Adventure"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l2[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Fantasy"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l3[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Science Fiction"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l4[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Crime"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l5[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Drama"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l6[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Thriller"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l7[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Animation"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l8[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Family"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l9[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Comedy"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l10[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Romance"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l11[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Horror"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l12[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "History"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l13[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "War"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l14[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Music"):
        for o in range(0, 5):
            label = tk.Label(app, text=(o + 1, mov_l15[o])).place(x=X, y=Y)
            Y += 30
    elif (q == "Documentary"):
        for o in range(0, 5):
            print(mov_l16[o])
            label = tk.Label(app, text=(o + 1, mov_l16[o])).place(x=X, y=Y)
            Y += 30
    else:
        label = tk.Label(app, text="Nothing to show").place(x=470, y=112)


def showdir():
    m = cl_1.get()
    q = str(m)
    ch=["Following","Dark Knight","Dark Knight Rises","Inception","Interstellar"]
    jc=["Terminator","Titanic","True Lies","Avatar Way of water","Piranha"]
    ms=["Departed","Wolf of the Wall Street","Irish Man","Aviator","Taxi Driver"]
    qt=["Django","Pulp fiction","Ig.Bastards","Once upon a time in hollywood","kill bill series"]
    pj=["Hobbit Series","King Kong","Mortal Engines","Braindead","Lord of rings series"]
    df=["Social Network","The Benjamin Case","Gone Girl","The game","Panic Room"]

    Y=370
    if(q=="Chris. Nolan"):
        for o in range(0, len(ch)):
            label = tk.Label(app, text="Chris. Nolan Movies").place(x=400, y=340)
            label = tk.Label(app, text=(o + 1, ch[o])).place(x=400, y=Y)
            Y += 30
    elif(q=="James Cameron"):
        for o in range(0, len(ch)):
            label = tk.Label(app, text="James Cameron Movies").place(x=400, y=340)
            label = tk.Label(app, text=(o + 1, jc[o])).place(x=400, y=Y)
            Y += 30
    elif (q == "Martin Scorsese"):
        for o in range(0, len(ch)):
            label = tk.Label(app, text="Martin Scorsese Movies").place(x=400, y=340)
            label = tk.Label(app, text=(o + 1, ms[o])).place(x=400, y=Y)
            Y += 30
    elif (q == "Q. Tarantino"):
        for o in range(0, len(ch)):
            label = tk.Label(app, text="Q. Tarantino Movies").place(x=400, y=340)
            label = tk.Label(app, text=(o + 1, qt[o])).place(x=400, y=Y)
            Y += 30
    elif (q == "David Fincher"):
        for o in range(0, len(ch)):
            label = tk.Label(app, text="David Fincher Movies").place(x=400, y=340)
            label = tk.Label(app, text=(o + 1, df[o])).place(x=400, y=Y)
            Y += 30
    elif (q == "Peter Jackson"):
        for o in range(0, len(ch)):
            label = tk.Label(app, text="Peter Jackson Movies").place(x=400, y=340)
            label = tk.Label(app, text=(o + 1, pj[o])).place(x=400, y=Y)
            Y += 30
    else:
        label = tk.Label(app, text="Nothing to Show").place(x=400, y=Y)


# Dropdown menu options
options = [
    'Action',
    'Adventure',
    'Fantasy','Science Fiction',
    'Crime','Drama','Thriller',
    'Animation','Family',
    'Comedy','Romance','Horror',
    'History','War',
    'Music','Documentary']
app=tk.Tk()
name_var=tk.StringVar()
app.title("MoviePop")
app.geometry("800x540")
label=tk.Label(app,text="MoviePop")
label.pack()
label1=tk.Label(app,text="Search Your Play",padx=20, pady=20).place(x=20,y=30)
label2=tk.Label(app,text="Search Genres",padx=20, pady=20).place(x=420,y=30)
entry=tk.Entry(app,textvariable=name_var).place(x=40,y=70)
#n=entry.get()
button=tk.Button(app,text="🔍",command=play,activebackground="red",activeforeground="blue").place(x=170,y=70)
clicked = tk.StringVar()

# initial menu text
clicked.set("Action")

# Create Dropdown menu
drop = tk.OptionMenu(app, clicked, *options).place(x=470,y=70)
#drop.pack()

# Create button, it will change label text
button = tk.Button(app, text="📝", command=show).place(x=590,y=70)

optionsdir = [
    'Chris. Nolan',
    'James Cameron',
    'Martin Scorsese',
    'Q. Tarantino',
    'David Fincher',
    'Peter Jackson'
]

cl_1=tk.StringVar()
cl_1.set("Chris. Nolan")
label3=tk.Label(app,text="Famous Directors Filmography",padx=20, pady=20).place(x=20,y=330)
drop_1 = tk.OptionMenu(app, cl_1, *optionsdir).place(x=45,y=370)
#drop.pack()

# Create button, it will change label text
button_1 = tk.Button(app, text="📝", command=showdir).place(x=165,y=370)
# Create Label
label = tk.Label(app, text=" ")
label.pack()
app.mainloop()