nome = "KeViN"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!   "

menu = "Python"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(14), "#")
print("p-y-t-h-o-n")

for letra in menu:
    print(letra,end="-")
    print("-".join(menu))