print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 22
total_de_tentativas = 3

# range(start, stop, [step])
# parâmetro "stop" não é inclusivo. ex: range(1,3) gera 2 iterações

# for não deve ter parênteses

for tentativa in range(1, total_de_tentativas + 1):
    print("-- Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute_str = input("- Digite um número entre 1 e 100:")
    chute = int(chute_str)

    if (chute < 1):
        print("- Número inválido. Digite um número acima de 1.")
        continue
    elif (chute > 100):
        print("- Número inválido. Digite um número abaixo de 100.")
        continue

    print("- Você digitou", chute)

    chute_certo = (chute == numero_secreto)
    chute_maior = (chute > numero_secreto)
    chute_menor = (chute < numero_secreto)

    if (chute_certo):
        print("- Parabéns, certa resposta!")
        break  # sai do laço for
    else:
        if (chute_maior):
            print("- ERROU! Seu chute foi maior que o número secreto.")
        elif (chute_menor):
            print("- ERROU! Seu chute foi menor que o número secreto.")

print("**** Fim do jogo ****")
