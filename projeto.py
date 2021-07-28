from tkinter import *

def temporizador():
    def ciclo():
        global rodando;global segundos;global minutos;global horas;global dias
        if rodando == True:
            lb_relogio['text']= f'{dias}d {horas}h {minutos}m {segundos}s'  
            lb_relogio.after(1000, ciclo) #mecanissmo de regressão dos segundos a cada 1000 milisegundos
            if horas == 0 and dias > 0 and minutos == 0 and segundos == 0:
                horas = 24;dias -= 1;lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s'                   
            if minutos == 0 and horas > 0 and segundos == 0:
                minutos = 60;horas -= 1;lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s' 
            if segundos == 0 and minutos > 0:
                segundos = 60;minutos -= 1;lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s' 
            if dias == 0 and horas == 0 and minutos == 0 and segundos <= 0:
                rodando = False
            segundos -= 1 #contador de regressão dos segundos
    ciclo()

def criar():
    global rodando;rodando = True
    global dias;dias = int(et_d.get())
    global horas;horas = int(et_h.get())
    global minutos;minutos = int(et_m.get())
    global segundos;segundos = int(et_s.get())
    if dias+horas+minutos+segundos > 0:
        lb_relogio['text']=f'{dias}d {horas}h {minutos}m {segundos}s' 
        temporizador()
        bt_criar['state']='disabled'
        bt_pausar['state']='normal'
        bt_fechar['state']='normal'
    
def pausar():
    global rodando
    global pausado;pausado = 1
    if pausado == 1:
        rodando = False
        pausado = 2
        bt_pausar['text'] = 'Retornar'
        pass
        
def retornar():
    global rodando
    global pausado
    if pausado == 2:
        rodando = True
        pausado = 1
        bt_pausar['text'] = 'Pausar'

def fechar():
    global rodando
    rodando = False
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
janela.configure(bg='green')

#Menu de Criação
lb_parametro = Label(janela,text="Defina os parâmetros desejados"); lb_parametro.grid(column=0,row=0,columnspan=7,pady=15)
lb_d = Label(janela,text="d"); lb_d.grid(column=1,row=1,sticky=W+E)
lb_h = Label(janela,text="h"); lb_h.grid(column=3,row=1,sticky=W+E)
lb_m = Label(janela,text="m"); lb_m.grid(column=5,row=1,sticky=W+E)
lb_s = Label(janela,text="s"); lb_s.grid(column=7,row=1,sticky=W+E)
et_d = Entry(janela,width=2); et_d.insert(0,"0"); et_d.grid(column = 0, row = 1)
et_h = Entry(janela,width=2); et_h.insert(0,"0"); et_h.grid(column = 2, row = 1)
et_m = Entry(janela,width=2); et_m.insert(0,"0"); et_m.grid(column = 4, row = 1)
et_s = Entry(janela,width=2); et_s.insert(0,"0"); et_s.grid(column = 6, row = 1)
bt_criar = Button(janela,width=30,text="Criar",command=criar) ; bt_criar.grid(column=0,row=2,columnspan=7,pady=15)

#Timer
lb_relogio = Label(janela,text='0d 0h 0m 0s',fg='white',bg='black',height=4); lb_relogio.grid(column=0,row=3,columnspan=7,sticky=W+E)
bt_pausar = Button(janela,width=5,text="Pausar",command=pausar,state='disabled') ; bt_pausar.grid(column=2,row=4, columnspan=2,sticky=W+E)
bt_fechar = Button(janela,width=5,text="Fechar",command=fechar,state='disabled') ; bt_fechar.grid(column=4,row=4, columnspan=2,sticky=W+E)

janela.mainloop()