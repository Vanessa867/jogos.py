def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]

    jogador1 = input("Jogador1, escolha pedra, papel ou tesoura: ")

    jogador2 = input("Jogador2, escolha pedra, papel ou tesoura: ")

    if jogador1 and jogador2 not in opcoes:
        print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
        return

    print(f"Você escolheu: {jogador1}")
    print(f"O computador escolheu: {jogador2}")

    if jogador1 == jogador2:
        print("Empate!")
    elif (
        (jogador1 == "pedra" and jogador2 == "tesoura")
        or (jogador1 == "papel" and jogador2 == "pedra")
        or (jogador1 == "tesoura" and jogador2 == "papel")
    ):
        print("Jogador1 ganhou!")
    else:
        print("Jogador2 ganhou!")

jogar_jokenpo()
