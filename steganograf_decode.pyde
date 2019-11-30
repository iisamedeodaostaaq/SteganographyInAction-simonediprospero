#dichiaro le variabili relative alla finestra
b_width = 500
b_height = 500

def setup():
    background(255)
    size(b_width,b_height)
    img = loadImage("steganografia.tiff")
    image(img, 0, 0) #visualizza img
    decode(img) 

# funzione decode immagine    
def decode(img):
    img.loadPixels() #carica i pixel dell'immagine in pixels[]array
    frase=""
    i=0
    k=0
    j=0
    width_img=img.width # larghezza img
    height_img=img.height # altezza img
    while (i<(width_img*height_img)): 
        r=red(img.pixels[i]) #code red
        g=green(img.pixels[i]) #code green
        b=blue(img.pixels[i]) #code blue
        frase=frase+chr(int(r))+chr(int(g))+chr(int(b)) #converto i colori in caratteri, tramite chr
        i+=50
        if (i%width==0): # quando ho terminato di decodificare la riga 
            i=i+width_img*(50-1) #passo alla riga successiva
        if r==0 and g==0 and b==0: #se il colore è nero la frase è terminata
            break
    print(frase)   #stampo la frase iniziale
