texto =(input("Escribe una frase")) 

vocal = ("A","E","I","O","U","a","e","i","o","u") 
numero_vocal = 0 
for letra in texto:
    if(letra in vocal):
        numero_vocal +=1
print("El numero de vocales es", numero_vocal)
