conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
     print("Saque realizado com sucesso!")
elif saque <= (saldo + cheque_especial):
    print("Saque realizado com check especial!")
    