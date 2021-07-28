from tkinter import *
import pygame
pygame.init()
pygame.mixer.music.load('beep.mp3')

def temporizador():
    def ciclo():
        global rodando,segundos,minutos,horas,dias
        if rodando == True:
            lb_relogio['text']= f'{dias}d {horas}h {minutos}m {segundos}s'  
            lb_relogio.after(1000, ciclo) #mecanissmo de regressão dos segundos a cada 1000 milisegundos
            if horas == 0 and dias > 0 and minutos == 0 and segundos == 0:
                horas = 24;dias -= 1;lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s'                   
            if minutos == 0 and horas > 0 and segundos == 0:
                minutos = 60;horas -= 1;lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s' 
            if segundos == 0 and minutos > 0:
                segundos = 60;minutos -= 1;lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s'
            if dias+horas+minutos+segundos <=0:
                rodando = False
            segundos -= 1 #contador de regressão dos segundos
            if rodando == False and dias+horas+minutos+segundos <=0:
                pygame.mixer.music.play(loops=-1)
    ciclo()

def criar():
    global rodando,dias,horas,minutos,segundos
    rodando = True
    dias = int(et_d.get())
    horas = int(et_h.get())
    minutos = int(et_m.get())
    segundos = int(et_s.get())
    if dias+horas+minutos+segundos > 0:
        lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s' 
        temporizador()
        bt_criar['state']='disabled'
        bt_pausar['state']='normal'
        bt_fechar['state']='normal'
    
def pausar():
    global rodando
    if bt_pausar['text'] == 'Pausar':
        rodando = False
        bt_pausar['text'] = 'Retornar'
    else:
        rodando = True
        temporizador()
        bt_pausar['text'] = 'Pausar'
    janela.update()

def fechar():
    global rodando
    pygame.mixer.music.stop()
    rodando = False
    bt_pausar['text'] = 'Pausar'
    #zera os campos do relógio e dos entrys do menu.
    lb_relogio['text'] = '0d 0h 0m 0s'
    et_d.delete(0,'end'); et_d.insert(0,'0')
    et_h.delete(0,'end'); et_h.insert(0,'0')
    et_m.delete(0,'end'); et_m.insert(0,'0')
    et_s.delete(0,'end'); et_s.insert(0,'0')
    bt_pausar['state']='disabled'
    bt_fechar['state']='disabled'
    bt_criar['state']='normal'
    
janela = Tk()
janela.title("SimpleTimer")
altura_tela = janela.winfo_screenheight()
largura_tela = janela.winfo_screenwidth()
janela.geometry(f"300x300+{altura_tela//2}+100")
janela.resizable(False, False)
janela.configure(bg='yellow')

#Menu de Criação
lb_x = Label(janela,text="          ",bg='yellow').grid(column=0)
lb_parametro = Label(janela,text="Defina os parâmetros desejados",font='normal 11 bold',bg='yellow'); lb_parametro.grid(column=2,row=0,columnspan=100,pady=15)
lb_d = Label(janela,text="        d",bg='yellow'); lb_d.grid(column=3,row=1,sticky=E)
lb_h = Label(janela,text="h",bg='yellow'); lb_h.grid(column=4,row=1,sticky=E)
lb_m = Label(janela,text="m",bg='yellow'); lb_m.grid(column=5,row=1,sticky=E)
lb_s = Label(janela,text="        s",bg='yellow'); lb_s.grid(column=6,row=1,sticky=E)
et_d = Entry(janela,width=2); et_d.insert(0,"0"); et_d.grid(column = 3, row = 1)
et_h = Entry(janela,width=2); et_h.insert(0,"0"); et_h.grid(column = 4, row = 1)
et_m = Entry(janela,width=2); et_m.insert(0,"0"); et_m.grid(column = 5, row = 1)
et_s = Entry(janela,width=2); et_s.insert(0,"0"); et_s.grid(column = 6, row = 1)
bt_criar = Button(janela,width=30,text="Criar",command=criar) ; bt_criar.grid(column=2,row=2,columnspan=7,pady=15)

#Timer
lb_relogio = Label(janela,text='0d 0h 0m 0s',font='normal 20',fg='white',bg='black'); lb_relogio.grid(column=2,row=3,columnspan=7,sticky=W+E)
bt_pausar = Button(janela,width=5,text="Pausar",command=pausar,state='disabled') ; bt_pausar.grid(column=4,row=4,columnspan=1,sticky=W+E)
bt_fechar = Button(janela,width=5,text="Fechar",command=fechar,state='disabled') ; bt_fechar.grid(column=5,row=4,columnspan=1,sticky=W+E)

janela.mainloop()