#Aluno: Gustavo Donato - Questão: "horas e minutos"

A = int(input("Digite o ângulo inteiro A entre 0 e 180 que você deseja encontrar: "))

while True:
    #olha se é meio-dia ou meia-noite
    if A == 0 or A == 180:
        print("y")
        break

    # não ocorre em nenhum outro momento
    if A % 180 == 0:
        print("n")
        break

    if A <= 30 or A >= 150:
        # todas as horas entre 1 e 11, os ponteiros estão sempre próximos
        print("y")
        break

    #definindo que o 90 é um angulo fixo
    if A == 90:
        print("y")
        break

    # limita até onde os ponteiros podem ir e calcula a diferença entre ele para verificar se o angulo realmente existe ou não
    for m in range(1, 720):
        vai = 6 * m
        logo = 0.5 * m
        ab = abs(vai - logo)

        #a diferença não pode ser maior ou igual que 180, logo tem dar uma ajeitada
        if ab >= 180:
            ab = 360 - ab

        if ab == A:
            print("y")
            break

    # caso nada disso ocorra o angulo não corresponde
    print("n")
    break
