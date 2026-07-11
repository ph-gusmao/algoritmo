# Simples, Composto, Encadeado

n1 = nota2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Calcular a média aritmética das notas
media = (n1 + n2) / 2

if media >= 7.0:
    print("Resultado: Aprovado!")
elif media >= 5:
    print("Você está em recuperação!")
else:
    print("Resultado: Reprovado!")

print("Sua média é: {}".format(media))
