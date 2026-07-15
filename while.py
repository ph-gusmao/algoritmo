# num = 1

# while num <= 100:
#     print(num)
#     num = num + 1
#     # ou num += 1

nome = None

while True:
    nome = input("Digite seu nome, ou X para sair: ")

    if nome == "x" or nome == "X":
        break
    else:
        print(f"Bem vindo, {nome}")
print("Obrigado!")
