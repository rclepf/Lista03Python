contador = 0
pares = 0
impares = 0

while contador < 10:
    numero = int(input(f"Informe o {contador + 1}º número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
