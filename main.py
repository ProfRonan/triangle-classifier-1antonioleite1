n1 = int(input("Digite um número inteiro"))
n2 = int(input("Digite outro número inteiro"))
n3 = int(input("digite mais um n´mer inteiro"))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if n1 == n2 and n1 == n3:
        print("Equilátero")
    elif n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 != n1:
        print("Isósceles")
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print("Escaleno")
else:
    print("Não é um triângulo")
