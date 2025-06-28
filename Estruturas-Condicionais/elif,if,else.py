MAIOR_IDADE = 18
IDADE_ESPECIAL = 13

idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar a CNH.")
    
    
if idade >= IDADE_ESPECIAL:
    print("Voce ja tem idade para tirar sua CNH." )
elif idade == IDADE_ESPECIAL:
    print("voce nao pode tirar a CNH." )