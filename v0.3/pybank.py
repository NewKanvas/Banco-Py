from login import banco


# BANCO DE DADOS
contas = ["joão", "douglas"]  # joão so entra se for tudo minusculo (CONCERTEI)
senhas = ["1234", "2345"]
saldo = [1000, 500]
renda = [1350, 1350]
fatura = [600, 600]


moedas = ["NitCoin", "Elitium", "NyanCoin"]
valorM = [4.53, 20.83, 10.03]
valorIn = [[0, 0, 0], [0, 0, 0]]

sorte = [1, -1, 1]
v = [0, 0, 0]

# INIT

banco(contas, senhas, saldo, fatura, valorM, sorte, v, renda, moedas, valorIn)
