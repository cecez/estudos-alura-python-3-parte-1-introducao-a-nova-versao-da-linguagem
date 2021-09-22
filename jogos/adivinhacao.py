print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 22

# entrada sempre vem como str
chute_str = input("Digite seu número:")

# conversão str para int
chute = int(chute_str)

print("Você digitou", chute)

# para comparação ter sentido, variáveis precisam ter o mesmo tipo
if(numero_secreto == chute):
    print("Parabéns, certa resposta!")
else:
    print("ERROU! Mais sorte para você.")
