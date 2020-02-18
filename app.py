#importar framework
import cv2

#ler uma imagem
imagem = cv2.imread("cachorro.jpg")

#print(imagem)
# Mostra o shape (altura, largura, canais [RGB])
print(imagem.shape)

imagem[100, 300] = (0,0,255)

(b,g,r) = imagem[110,305]
print("Azul= ", b, " verde= " , g , " Vermelho= ", r)

imagem[100:150, 300:310] = (240,0,0)

#mostrar uma imagem
cv2.imshow("nomedawindow", imagem)


imagem2 = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("novawindow", imagem2)

#salvar uma imagem
cv2.imwrite("nnovaimagem.jpg", imagem)

#aguardar tecla ser pressionada
cv2.waitKey(0)

#destruir todas as janelas / certa janela
cv2.destroyAllWindows() 
