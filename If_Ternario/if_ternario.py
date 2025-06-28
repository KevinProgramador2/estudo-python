saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(F"{status} ao realizar o saque!")