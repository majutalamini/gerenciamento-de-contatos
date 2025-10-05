import time
import random

numero_sorteado = random.randint(1,100)

print("===== JOGO INTERATIVO =====")
print("1 . Iniciar jogo")
print("2 . Sair do jogo")
print("===========================")

try:
    escolha = int(input("Escolha uma opção(1 ou 2): "))

except ValueError:
    print("Entrada inválida. Por favor, digite 1 ou 2.")
    exit() 

while True:
    if escolha == 1:
        print("Ótimo! Você escolheu iniciar o jogo interativo. ")
        print("                ")
        print("Carregando jogo . . . ") 
        time.sleep(2)
        print("Pronto para jogar!")
        time.sleep(2)

        print("1 - PRIMEIRO JOGO: acertar o número aleatório de 1 a 100.")

        numero = int(input("Insira o número: "))

        time.sleep(0.5)

        while True:

            if numero_sorteado < numero:
                print(f"{numero} é maior que o número sorteado. Tente outra vez!")
                numero = int(input("Insira o número: "))
            
            elif numero_sorteado > numero:
                print(f"{numero} é menor que o número sorteado. Tente outra vez!")
                numero = int(input("Insira o número: "))

            else:
                print("Parabéns! Você acertou o número")

                time.sleep(2)
                print("Carregando próxima fase . . .")
                time.sleep(2)

                print("2 - SEGUNDO JOGO - Você está pronto para a próxima fase! Agora vamos jogar pedra, papel e tesoura!")

                escolha = str(input("Você escolhe pedra, papel ou tesoura? "))

                if escolha == "pedra":
                    

                break
    break

        



        