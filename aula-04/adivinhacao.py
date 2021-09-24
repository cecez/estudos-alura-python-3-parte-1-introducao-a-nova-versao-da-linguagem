print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 22
total_de_tentativas = 3
tentativa = 1

while (tentativa <= total_de_tentativas):
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute_str = input("Digite seu número:")
    chute = int(chute_str)

    print("Você digitou", chute)

    chute_certo = (chute == numero_secreto)
    chute_maior = (chute > numero_secreto)
    chute_menor = (chute < numero_secreto)

    if (chute_certo):
        print("Parabéns, certa resposta!")
    else:
        if (chute_maior):
            print("ERROU! Seu chute foi maior que o número secreto.")
        elif (chute_menor):
            print("ERROU! Seu chute foi menor que o número secreto.")

    tentativa = tentativa + 1
