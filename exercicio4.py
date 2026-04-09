class Exercicio4:
    """Algoritmo que apresenta um menu interativo com operações aritméticas"""
    
    def menu_calculadora(self):
        print("\n=== CALCULADORA ====")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = int(input("\nEscolha uma opção (1-5): "))

        if opcao == 5:
            print("Encerrando a calculadora...")

        elif opcao < 1 or opcao > 5:
            print("Opção inválida! Escolha entre 1 e 5.")

        else:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                resultado = num1 + num2
                print(f"\nResultado: {num1} + {num2} = {resultado}")

            elif opcao == 2:
                resultado = num1 - num2
                print(f"\nResultado: {num1} - {num2} = {resultado}")

            elif opcao == 3:
                resultado = num1 * num2
                print(f"\nResultado: {num1} × {num2} = {resultado}")

            elif opcao == 4:
                if num2 == 0:
                    print("\nERRO: Divisão por zero não é permitida!")
                else:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} ÷ {num2} = {resultado:.2f}")


if __name__ == "__main__":
    exercicio = Exercicio4()
    exercicio.menu_calculadora()