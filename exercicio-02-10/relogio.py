from datetime import time, datetime;

from tkinter import *
import tkinter
from datetime import datetime, time

##############################  Cores   ##############################
cor1 = "#3d3d3d"  # Preto
cor2 = "#fafcff"  # Branco
cor3 = "#21c25c"  # Verde
cor4 = "#eb463b"  # Vermelho
cor5 = "#dedcdc"  # Cinza
cor6 = "#3080f0"  # Azul

fundo = cor1
cor = cor4

janela=Tk()
janela.title("")
janela.geometry("600x200")
janela.resizable(width=False, height=False)
janela.configure(bg=cor1)


######################################################################





def relogio():

    tempo = datetime.now()
    horarios = datetime.now().strftime("%H:%M:%S")
    hora = tempo.strftime("%H:%M:%S")

    l1.config(text=hora)
    l1.after(200, relogio)

        

l1 = Label(janela, text="", font=("Arial 110"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()


    