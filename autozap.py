from tkinter import *

#criar janela
tela = Tk()
#titulo da janela
tela.title("Autozap")
#tamanho da tela
tela.geometry("800x600")
#cor de fundo
tela.configure(background="white")
#mudar tamanho da tela
tela.resizable(width=False,height=False)
#transparencia da tela
tela.attributes("-alpha",0.9)
#icone da janela
tela.iconbitmap(default="iconezap.ico")

logo = PhotoImage(file="imagezap.png")




leftframe = Frame(tela, width=305,height=600,bg="#25D366", relief="raise")
#posiçao da frame
leftframe.pack(side=LEFT)

#frameazuldireita
leftframe = Frame(tela, width=490,height=600,bg="#25D366", relief="raise")
#posiçao da frame
leftframe.pack(side=RIGHT)
#a logo
logolabel = Label(tela, image=logo, bg="#25D366")
logolabel.place(x=25,y=170)

autozap = Label(tela, text="AUTOZAP", font=("Sans-Serif",30),bg="#25D366", fg="white")
autozap.place(x=460,y=50)

mensagemlabel = Label(tela, text="Mensagem:", font=("Sans-Serif",20),bg="#25D366", fg="white")
mensagemlabel.place(x=320,y=130)

mensagementry = Entry(tela,width=30)
mensagementry.place(x=465,y=142)

contatolabel = Label(tela, text="contato:", font=("Sans-Serif",20),bg="#25D366", fg="white")
contatolabel.place(x=320,y=200)

contatoentry = Entry(tela,width=36)
contatoentry.place(x=425,y=212)

contatoinfo = Label(tela, text="Separe os números por vírgula", font=("Sans-Serif",10),bg="#25D366", fg="white")
contatoinfo.place(x=435, y=240)

vezeslabel = Label(tela, text="Nº Vezes:", font=("Sans-Serif",20),bg="#25D366", fg="white")
vezeslabel.place(x=320,y=280)

vezesentry = Spinbox(tela,width=31 ,from_=1, to=100)
vezesentry.place(x=445,y=292)

def start():
    mensagem = mensagementry.get()
    numero = contatoentry.get()
    quantidade = vezesentry.get()
    if not mensagem.strip():
        print("Por favor, insira uma mensagem.")
        return
    if not numero.strip():
        print("Por favor, insira um contato.")
        return
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        print("Por favor, insira um número válido para a quantidade.")
        return

     # Divida os contatos por vírgula e remova espaços em branco
    lista_contatos = [numero.strip() for numero in numero.split(",")]    

    print(f"Enviando mensagem para os contatos: {lista_contatos}")
    for numero in lista_contatos:
        print(f"Enviando para {numero}...")
    

botaolabel = Button(tela,text='Start',width=20,command=start)
botaolabel.place(x=600,y=540)

# Vincular a tecla Enter ao botão
tela.bind('<Return>', lambda event: start())

# Vincular a tecla Esc para fechar a janela
tela.bind('<Escape>', lambda event: tela.destroy())

tela.mainloop()
