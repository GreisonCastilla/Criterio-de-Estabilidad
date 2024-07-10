from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import math
from matplotlib.figure import Figure
import numpy as np
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

mA=[[Entry,Entry], [Entry, Entry]]
sol=[Entry, Entry, Entry]

def solucion():
    try:
        a1 = float(mA[0][0].get())
        a2 = float(mA[1][0].get())
        b1 = float(mA[0][1].get())
        b2 = float(mA[1][1].get())

        x1= 0.0
        x2 = 0.0

        for x in sol:
            x.configure(state="normal")
            x.delete(0, END)

        det = (a1*b2) - (a2*b1)
        t = a1+b2
        dis = (t**2) - (4*det)

        if(det==0):
            sol[2].insert(1, "Puntos Criticos Multiples")
        elif dis>= 0:
            if dis==0:
                x1=t/2
                x2=t/2
            else:
                x1=(t+math.sqrt(dis))/2
                x2=(t-math.sqrt(dis))/2
            
            if ((x1>0)and(x2>0)):
                sol[2].insert(1, "Nodo - Inestable")
            elif((x1<0)and(x2<0)):
                sol[2].insert(1, "Nodo - Estable")
            else:
                sol[2].insert(1, "Silla - Inestable")
                
        else:
            if(t==0):
                pi=math.sqrt(abs(dis))/2
                x1=str(pi)+"i"
                x2=str(-pi)+"i"
                sol[2].insert(1, "Centro - Estable")
            else:
                pr=t/2
                pi=math.sqrt(abs(dis))/2
                x1=str(pr)+" + "+str(pi)+"i"
                x2=str(pr)+" - "+str(pi)+"i"

                if t>0:
                    sol[2].insert(1, "Foco - Inestable")
                else:
                    sol[2].insert(1, "Foco - Estable")
                
        if det != 0:
            sol[0].insert(1, x1)
            sol[1].insert(1, x2)

        for x in sol:
            x.configure(state="readonly")
        
        graficar(a1, a2, b1, b2)
    except ValueError:
        messagebox.showinfo("Error", "Ingrese datos númericos")

def sistema(x, y, a1, a2, b1, b2):
    dxdt=a1*x + b1*y
    dydt=a2*x + b2*y
    return dxdt, dydt

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def graficar(a1, a2, b1, b2):
    
    limpiar_frame(g)

    t = np.linspace(0, 10, 2000)
    xi = np.linspace(-5, 5, 20)
    yi = np.linspace(-5, 5, 20)

    x, y = np.meshgrid(xi, yi)
    dx, dy= sistema(x, y, a1, a2, b1, b2)

    norm = np.sqrt(dx**2 + dy**2)
    dx/=norm
    dy/=norm

    fig = Figure(figsize=(5.6,4.5))
    sub = fig.add_subplot(111)
    sub.quiver(x, y, dx, dy, norm)
    
    #sub.set_ylabel("y")
    #sub.set_xlabel("x")

    sub.set_xlim(-5, 5)
    sub.set_ylim(-5, 5)

    canva = FigureCanvasTkAgg(fig, master=g)
    canva.draw()
    canva.get_tk_widget().place(relx=0.0, rely=-0.1)

def limpiar():
    for i in sol:
        i.configure(state="normal")
        i.delete(0, END)
        i.configure(state="readonly")
    
    for i in mA:
        for j in i:
            j.delete(0, END)

    limpiar_frame(g)

def panel1():
    p1 = Frame(ven, width=340, height=200, background="white")
    p1.place(relx=.02, rely=0.09)

    tp1 = Label(p1, text="Sistema de Ecuaciones", font=fuente, background="white")
    tp1.place(relx=.02, rely=0.02)

    return p1

def panel1_1 ():
    p1_2 = Frame(p1, width=250, height=100, background="RoyalBlue4")
    p1_2.place(relx=.13, rely=0.2)

    l1p1 = Label(p1_2, text=r"x'=           x+          y", font=fuente, foreground="White", background="RoyalBlue4")
    l1p1.place(relx=.15, rely=0.15)

    mA[0][0] = Entry(p1_2,width=4, font=fuente, background="White")
    mA[0][0].place(relx=.29, rely=0.15)

    mA[0][1] = Entry(p1_2,width=4, font=fuente, background="White")
    mA[0][1].place(relx=.59, rely=0.15)

    l2p1 = Label(p1_2, text=r"y'=           x+          y", font=fuente, foreground="White", background="RoyalBlue4")
    l2p1.place(relx=.15, rely=0.55)

    mA[1][0] = Entry(p1_2,width=4, font=fuente, background="White")
    mA[1][0].place(relx=.29, rely=0.55)

    mA[1][1] = Entry(p1_2,width=4, font=fuente, background="White")
    mA[1][1].place(relx=.59, rely=0.55)

def panel2():
    p2= Frame(ven,width=340, height=300, background="white")
    p2.place(relx=.02, rely=0.45)

    tp2 = Label(p2, text="Respuesta", font=fuente, background="white")
    tp2.place(relx=0.02, rely=0.02)
    return p2

def panel2_1():
    p2_1 = Frame(p2, width=260, height=180, background="RoyalBlue4")
    p2_1.place(relx=.12, rely=.19)

    l1 = Label(p2_1, text="\u03bb\u2081 =", font=fuente, background="RoyalBlue4", foreground="White")
    l1.place(relx=0.15, rely=0.2)

    sol[0] = Entry(p2_1, width=13, font=fuente, state="readonly")
    sol[0].place(relx=.32, rely=.2)

    l2 = Label(p2_1, text="\u03bb\u2082 =", font=fuente, background="RoyalBlue4", foreground="White")
    l2.place(relx=0.15, rely=0.45)

    sol[1] = Entry(p2_1, width=13, font=fuente, state="readonly")
    sol[1].place(relx=.32, rely=.45)
    
    l3 = Label(p2_1, text="Tipo", font=fuente, background="RoyalBlue4",foreground="white")
    l3.place(relx=.05, rely=.68)

    sol[2] = Entry(p2_1, width=19, font=fuente, state="readonly")
    sol[2].place(relx=.2, rely=.68)

    return sol

def panel3():
    p3 = Frame(ven, width=600, height=522, background="White")
    p3.place(relx=.38, rely=0.09)

    tp3 = Label(p3, text="Grafica", font=fuente3, background="white")
    tp3.place(relx=0.45, rely=0.05)
    return p3

def panel3_2():
    p3_2 = Frame(p3, width=550, height=430, background="white")
    p3_2.place(relx=0.04, rely=0.15)
    return p3_2

ven = Tk()
ven.title("Criterio de Estabilidad")
ven.geometry("1000x620+300+50")
ven.resizable(width=False, height=False)
fuente2 = Font(family="Tw Cen MT", size=28, weight="bold")
fuente3 = Font(family="Tw Cen MT", size=20, weight="bold")
fuente = Font(family="Tw Cen MT", size=14)
fuenteB = Font(family="Tw Cen MT", size=12)

titulo = Label(ven, text="Criterio de Estabilidad", font=fuente2)
titulo.pack()

creditos = Label(ven, text="Integrantes: Greison Rey Castilla Carmona, Orlando Mo Chen, Andres Quintana", font=fuenteB)
creditos.place(relx=.02, rely=.95)

#Panel 1
p1 = panel1()
boton1 = Button(p1, text="Resolver", background="RoyalBlue4",foreground="white" ,command= solucion,font=fuenteB)
boton1.place(relx=.48, rely=0.75)

boton2 = Button(p1, text="Limpiar", background="IndianRed3",foreground="white",command=limpiar, font=fuenteB)
boton2.place(relx=.69, rely=0.75)

#Panel 1_1
panel1_1()
#panel 2
p2 = panel2()
#panel 2_1
sol = panel2_1()
#panel 3
p3 = panel3()
#panel 3_2
g = panel3_2()

ven.mainloop()