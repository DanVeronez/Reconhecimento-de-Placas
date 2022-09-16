import cv2
import pytesseract
from lib import show_image 

kernel              = (5,5)
nivelDeDesfoque     = 100
todosContornos      = cv2.RETR_TREE
contornosFechados   = cv2.CHAIN_APPROX_NONE
pegaTodos           = -1
verde               = (0,255,0)
espessura           = 2
quadrilatero        = 4

img = cv2.imread("carro4.jpg")
show_image('img', img)

# Deixa a imagem cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# show_image('cinza' , cinza)

# Binariza a imagem
ret, binary = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
# show_image('binary' , binary)

# Desfoque na Imagem
desfoque = cv2.GaussianBlur(binary, kernel, nivelDeDesfoque)
# show_image('Desfoque', desfoque)

# Encontra Contornos
contornos, hierarquia = cv2.findContours(desfoque, todosContornos, contornosFechados)

# Pinta contornos de Verde
# cv2.drawContours(img, contornos, pegaTodos, verde, espessura)
# show_image('Imagem com contornos', img)

# Separa os contornos e separa a imagem da placa do restante da imagem


for contorno in contornos:
    perimetro = cv2.arcLength(contorno, True)

    if perimetro > 120:

        contornoAproximadoDoFormatoReal = cv2.approxPolyDP(contorno, 0.03 * perimetro, True)

        #Contornar apenas um quadrado na imagem
        if len(contornoAproximadoDoFormatoReal) == quadrilatero:
            
            (posicaoInicial, posicaoFinal, altura, largura) = cv2.boundingRect(contorno)
            cv2.rectangle(img, (posicaoInicial, posicaoFinal), (posicaoInicial+altura, posicaoFinal+largura), verde, espessura)

show_image("Placa verde", img)

# Le a imagem e transforma em String
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(img)
# print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()