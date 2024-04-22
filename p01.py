numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
if numero1 < numero2:
    numero1, numero2 = numero2, numero1
if numero1 < numero3:
    numero1, numero3 = numero3, numero1
if numero2 < numero3:
    numero2, numero3 = numero3, numero2
print("Os números em ordem decrescente são:", numero1, numero2, numero3)