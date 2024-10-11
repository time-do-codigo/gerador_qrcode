import qrcode
import qrcode.constants
import io  
from PIL import Image, ImageTk
from tkinter import filedialog

text_input = ''

def gerador_qrcode():
    text = text_input.get()
    #Cria o objeto qrcode
    qr = qrcode.QRCode(
        version = 1, 
        error_correction =  qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
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
    img_byte = Image.open(io.BytesIO(img_buff)) # transforma os dados da imagem (que estão em formato de bytes) em um objeto de imagem do Pillow
    qr_image = ImageTk.PhotoImage(img_byte)  # converte essa imagem do Pillow em um objeto que pode ser exibido em uma interface Tkinter.
    
    #Exibe a imagem em uma etiqueta
    qr_label.config(image = qr_image)
    qr_label.image = qr_image #garante que o objeto da imagem não seja removido da memória enquanto ele ainda é necessário.
    
    #Salva a imagem como png
    file_path = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('Arquivos PNG','*.png')]
    )
    if file_path:
        with open(file_path,'wb') as f: #o arquivo deve ser aberto em forma de escrita binária
            f.write(img_buff)
        status_label.config(text=f'Arquivo salvo em {file_path}')
    
    
 
gerador_qrcode()  
     
    