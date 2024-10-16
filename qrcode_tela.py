import qrcode
import qrcode.constants
import io 
import validators
from PIL import Image as PILImage, ImageTk
from tkinter import filedialog
from tkinter import *

def validar_url(entrada):
    # Verifica se a URL é válida
    return validators.url(entrada)

def validar_entrada_usuario(texto_link):
    entrada = texto_link.strip()
    if validar_url(entrada):
        label_erro_url.config(text='A entrada é uma URL válida!', fg='green', bg='#3b3b3b')
    else:
        label_erro_url.config(text='A entrada não é uma URL válida. Será considerada como um texto comum.', fg='red', bg='#3b3b3b')
    return entrada

def gerador_qrcode():
    text = validar_entrada_usuario(texto_link.get())
    #Cria o objeto qrcode
    qr = qrcode.QRCode(
        version = 1, 
        error_correction =  qrcode.constants.ERROR_CORRECT_L,
        box_size = 6,
        border = 2,
    )
    #Adiciona texto ao qrcode
    qr.add_data(text)
    qr.make(fit=True)
    
    #Cria uma imagem do qrcode
    img = qr.make_image (
        fill_color = 'black',
        back_color = 'white'
    )
    #Cria um buffer de memoria 
    img_buff = io.BytesIO() 
    img.save(img_buff, format='PNG')
    img_buff = img_buff.getvalue()
    
    #Cria uma imagem visivel do qrcode
    img_byte = PILImage.open(io.BytesIO(img_buff)) # transforma os dados da imagem (que estão em formato de bytes) em um objeto de imagem do Pillow
    qr_image = ImageTk.PhotoImage(img_byte)  # converte essa imagem do Pillow em um objeto que pode ser exibido em uma interface Tkinter.
    
    #Exibe a imagem em uma etiqueta
    label_qr_code.config(image = qr_image)
    label_qr_code.image = qr_image #garante que o objeto da imagem não seja removido da memória enquanto ele ainda é necessário.
    
    #Salva a imagem como png
    file_path = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('Arquivos PNG','*.png')]
    )
    if file_path:
        with open(file_path,'wb') as f: #o arquivo deve ser aberto em forma de escrita binária
            f.write(img_buff)
        label_status.config(text=f'Arquivo salvo em:\n {file_path}')
    texto_link.delete(0, END)


#criação da janela

janela = Tk()
janela.geometry('600x600')
janela.title('Gerador de QR Code')
janela.iconbitmap('imagens/icone.ico')
janela.resizable(False, False)

frame = Frame(janela, bg='#3b3b3b')
frame.place(width=600, height=600)

titulo = Label(frame, text='Gerador QR Code', font=('Consolas', 24), bg='#3b3b3b', fg='#feffff')
titulo.pack(pady = 10)

texto1 = Label(frame, text='Insira o seu link para gerar', font=('Helvetica', 12), bg='#3b3b3b', fg='#feffff')
texto1.place(x=200, y=200)

texto_link = Entry(frame, text='', font=('bold', 12))
texto_link.place(x=100, y=230, width=400, height=28)

#imagens janela principal

#imagem logo
logo= PILImage.open('imagens/icons8-qr-code-100.png')
logo = logo.resize((140,140),PILImage.LANCZOS)
logo = ImageTk.PhotoImage(logo)
label_logo = Label(janela, image=logo, compound=LEFT, anchor='nw', bg='#3b3b3b') 
label_logo.place(x=220,y=50)


#lupa de pesquisa
logo1 = PILImage.open('imagens/link.png')
logo1 = logo1.resize((50,50), PILImage.LANCZOS)
logo1 = ImageTk.PhotoImage(logo1)
label_logo1= Label(janela, image=logo1, compound=LEFT, anchor='nw',bg='#3b3b3b')
label_logo1.place(x=40, y=220)

#imagem botao
logo2 = PILImage.open('imagens/botao_criar.png')
logo2 = logo2.resize((40,40), PILImage.LANCZOS)
logo2 = ImageTk.PhotoImage(logo2)
label_logo2= Button(janela, command=gerador_qrcode, image=logo2, compound=LEFT, anchor='nw',bg='#3b3b3b', bd=0, activebackground="#3b3b3b")
label_logo2.place(x=505, y=222)


# Label para exibir mensagem de URL inválida
label_erro_url = Label(janela, text="", font=('Helvetica', 10), fg='red', bg='#3b3b3b')
label_erro_url.place(x=100, y=260) 


# Label para exibir o QR Code gerado
frame_de_baixo = Frame(janela, width= 400, height= 250, bg='#3b3b3b')
frame_de_baixo.place(relx=0.5, rely=0.7, anchor='center')
label_qr_code = Label(frame_de_baixo, bg='#3b3b3b') 
label_qr_code.place(relx=0.5, rely=0.5, anchor='center')


# Label para exibir o status de salvamento
label_status = Label(janela, text="", font=('Helvetica', 12), bg='#3b3b3b', fg='#FFFFFF')
label_status.pack(side=BOTTOM, pady=10)  # Posiciona o status no fundo da janela

janela.mainloop() 




