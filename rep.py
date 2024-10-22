texto = input('Digite uma palavra: ')
vogais = 0
VOGAIS = 'aeiou' 

for letra in texto:
    if letra in VOGAIS:
        vogais += 1
        
print("As vogais encontradas são: ", end='')
for letra in texto:
    if letra in VOGAIS:
        print(letra, end=' ')
print() 
