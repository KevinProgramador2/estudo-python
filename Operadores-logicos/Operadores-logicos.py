# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True 

print(True and True)
print(True and False)
print(True or True or False)
print(True or False)
print(False or False or False)



saldo = 1000
saque = 250
limite = 200
conta_epecial = True

exp = saldo >= saque and saque <= limite or conta_epecial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque 
<= limite) or (conta_epecial and saldo >= saque)
print(exp_2)


conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_normal_com_saldo_suficiente = conta_epecial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_normal_com_saldo_suficiente  