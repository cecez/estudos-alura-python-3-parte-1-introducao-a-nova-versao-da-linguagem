print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 22

# entrada sempre vem como str no Python 3
chute_str = input("Digite seu número:")

# conversão str para int
chute = int(chute_str)

print("Você digitou", chute)

# condições mais legíveis
chute_certo = (chute == numero_secreto)
chute_maior = (chute > numero_secreto)
chute_menor = (chute < numero_secreto)

if(chute_certo):
    print("Parabéns, certa resposta!")
else:
    if(chute_maior):
        print("ERROU! Seu chute foi maior que o número secreto.")
    elif(chute_menor):
        print("ERROU! Seu chute foi menor que o número secreto.")