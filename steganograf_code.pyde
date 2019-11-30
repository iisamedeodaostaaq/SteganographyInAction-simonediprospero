#dichiaro le variabili relative alla finestra
b_width = 500
b_height = 500
# dimensione quadrato 50px
dimQuadrato=50


def setup():
    background(255)
    size(b_width,b_height)
    #inserisco in input il file di testo
    testo = open("prova.txt")
    fulltext= testo.read() #inserisco il testo in una variabie str provvisoria
    fulltext_array=[]
    #inserisco la frase in una lista
    for i in range (len(fulltext)):
        fulltext_array.append(fulltext[i])
    controllo(fulltext_array)
    ascii(fulltext_array)
    
def ascii(fulltext_array):
    ascii_array=[] 
    i=0
    for i in range (len(fulltext_array)): #fino alla lunghezza della frase
        elemento_ascii=ord(fulltext_array[i])
        ascii_array.append(elemento_ascii) #aggiungo gli elementi convertiti in ascii sulla lista
    
    quadrati(ascii_array)
    
        
def quadrati(ascii_array):
    quadrato=0
    i=0
    j=0
    k=0
    loadPixels()
    lunghezza=len(ascii_array)
    while (i < lunghezza/3): # fino a quando i è minore della lunghezza della lista
        
        r=ascii_array[0]
        g=ascii_array[1]
        b=ascii_array[2]
        
        for j in range(dimQuadrato):
            for k in range(dimQuadrato):
                pixels[quadrato+k+(width*j)]=color(r,g,b) #coloro  i quadrati
        quadrato+=dimQuadrato
        i=i+1
        del(ascii_array[:3]) #cancello i primi 3 lementi della lista
        
        if (quadrato%width==0):
            #se ho finito una riga di quadrati, il prossimo quadrato va posizionato sotto le dimTessera righe pixel
            quadrato=quadrato+b_width*(dimQuadrato-1)
            
        if not ascii_array: # se la lista è vuota 
            break
    # se non ho colorato tutta la riga, la coloro con quadrati neri    
    while (quadrato%width!=0):
        for j in range(dimQuadrato):
            for k in range(dimQuadrato):
                pixels[quadrato+k+(width*j)]=color(0,0,0)
        quadrato+=dimQuadrato
                    
    updatePixels()
    
    save("steganografia.tiff") #salvo l'immagine
    
#funzione per controllare se la frase è multipla di 3
def controllo(fulltext_array):
    if (len(fulltext_array)%3!= 0):
        if (len(fulltext_array)+1 %3== 0):
            fulltext_array.append(" ")
        else:
            fulltext_array.append(" ")
            controllo(fulltext_array)
    
