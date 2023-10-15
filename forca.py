palavra = "cachorro"
letras_usuarios = []
chances = 5
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuarios:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} tentativas")

    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuarios.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True  # Correção: Use apenas um único sinal de igual para atribuir True a ganhou
    for letra in palavra:
        if letra.lower() not in letras_usuarios:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns! você ganhou. A palavra era: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
