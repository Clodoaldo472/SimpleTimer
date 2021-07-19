from tkinter import *
from time import sleep

def _contagem():
    dias = int(ed2.get())*24*60*60
    horas = int(ed3.get())*60*60
    minutos = int(ed4.get())*60
    segundos = int(ed5.get())
    total = dias+horas+minutos+segundos

    for x in range (total, -1, -1):
        lb6["text"] = x
        sleep(1)

janela = Tk()
janela.title("MultiTimer")
janela.geometry("450x300+0+0")

lb1 = Label(janela,text="Defina os parâmetros desejados"); lb1.place(x=100,y=80)

ed2 = Entry(janela,width=3); ed2.place(x=100,y=120)
lb2 = Label(janela,text="d"); lb2.place(x=120,y=120)

ed3 = Entry(janela,width=3); ed3.place(x=135,y=120)
lb3 = Label(janela,text="h"); lb3.place(x=155,y=120)

ed4 = Entry(janela,width=3); ed4.place(x=170,y=120)
lb4 = Label(janela,text="m"); lb4.place(x=190,y=120)

ed5 = Entry(janela,width=3); ed5.place(x=210,y=120)
lb5 = Label(janela,text="s"); lb5.place(x=230,y=120)

bt1 = Button(janela,width=30,text="Criar", command=_contagem); bt1.place(x=100,y=150)

lb6 = Label(janela,text=""); lb6.place(x=100,y=200)


janela.mainloop()



'''

gerenciadores de layout: PLACE , PACK , GRID

#pegar valor do Entry
ed.get()


'''
