numero = int(input("Informe um número de 1 a 10: "))

if 1 <= numero <= 10:
    for i in range(1, numero + 1):
        print(i)
else:
    print("Número fora do intervalo permitido.")
