valor = int(input())
valorI =valor 
valor100 = 0
valor50 = 0
valor25 = 0
valor10 = 0
valor5 = 0
valor2 = 0
valor1 = 0 

valor100 = valor // 100
valor = valor % 100
valor50 = valor // 50 
valor = valor % 50
valor20 = valor // 20
valor = valor % 20
valor10 = valor // 10
valor = valor % 10
valor5 = valor // 5
valor = valor % 5
valor2 = valor // 2
valor = valor % 2
valor1 = valor // 1
valor = valor % 1
print(valorI)
print("{} nota(s) de R$ 100,00".format(valor100))
print("{} nota(s) de R$ 50,00".format(valor50))
print("{} nota(s) de R$ 20,00".format(valor20))
print("{} nota(s) de R$ 10,00".format(valor10))
print("{} nota(s) de R$ 5,00".format(valor5))
print("{} nota(s) de R$ 2,00".format(valor2))
print("{} nota(s) de R$ 1,00".format(valor1))