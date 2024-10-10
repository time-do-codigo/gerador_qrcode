from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

#criação da janela

janela = Tk()
janela.geometry('600x500')
janela.title('Gerador de QR Code')
janela.iconbitmap('imagens/icone.ico')

frame = Frame(janela, bg='#3b3b3b')
frame.place(width=600, height=500)

titulo = Label(frame, text='Gerador QR Code', font=('Consolas', 24), bg='#3b3b3b', fg='#feffff')
titulo.pack(pady = 10)

texto1 = Label(frame, text='Insira o seu link para gerar', font=('bold', 12), bg='#3b3b3b', fg='#feffff')
texto1.place(x=200, y=200)

texto_link = Entry(frame, text='', font=('bold', 12))
texto_link.place(x=80, y=230, width=400, height=25)

#imagens janela principal

#imagem logo
logo= Image.open('imagens/icons8-qr-code-100.png')
logo = logo.resize((140,140),Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)
label_logo = Label(janela, image=logo, compound=LEFT, anchor='nw', bg='#3b3b3b') 
label_logo.place(x=220,y=50)

#lupa de pesquisa
logo1 = Image.open('imagens/link.png')
logo1 = logo1.resize((50,50), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo1)
label_logo1= Label(janela, image=logo1, compound=LEFT, anchor='nw',bg='#3b3b3b')
label_logo1.place(x=20, y=217)

#imagem botao
logo2 = Image.open('imagens/botao_criar.png')
logo2 = logo2.resize((41,42), Image.LANCZOS)
logo2 = ImageTk.PhotoImage(logo2)
label_logo2= Button(janela, command='', image=logo2, compound=LEFT, anchor='nw',bg='#3b3b3b', bd=0, activebackground="#FFFFFF")
label_logo2.place(x=495, y=220)

janela.mainloop()