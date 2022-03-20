def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def menu():
    print("1. Soma \n2. Subtração \n3.Multiplicação \n4.Divisão \n5. Sair")
    op = int(input("Informe a opção desejada"))
    while (op<1 or op>5):
        print("Opção inválida")
        op = int(input("Informe a opção desejada"))
    return op

def escolha(op,n1,n2):
    if op == 1:
        result = soma(n1,n2)
    if op == 2:
        result = subtracao(n1,n2)
    if op == 3:
        result = multiplicacao(n1,n2)
    if op == 4:
        if n2 != 0:
            result = divisao(n1,n2)
        else:
            result = None
    return result

def entrada():
    return int(input())

def main():
    while True:
        op = menu()
        if op == 5:
            break
    print("Digite dois números")
    n1 = entrada()
    n2 = entrada()
    if escolha(op,n1,n2) == None:
        print("Não há divisão por zero")
    else:
        print(escolha(op,n1,n2))

main()
