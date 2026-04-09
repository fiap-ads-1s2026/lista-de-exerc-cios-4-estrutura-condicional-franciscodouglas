class Exercicio6:
    """Algoritmo que calcula o IMC e verifica se a pessoa está no peso ideal"""
    
    def calcular_imc(self):
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros: "))

        if peso <= 0 or altura <= 0:
            print("ERRO: Peso e altura devem ser valores positivos")
            return

        if altura > 3.0:
            print("ERRO: Altura muito alta. Digite a altura em metros (ex: 1.75)")
            return

        imc = peso / (altura ** 2)

        print(f"\nDados informados:")
        print(f"Peso: {peso:.1f} kg")
        print(f"Altura: {altura:.2f} m")
        print(f"\nÍndice de Massa Corporal (IMC): {imc:.1f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
            print("Status: NÃO está no peso ideal")
        elif 18.5 <= imc < 25:
            print("Classificação: Peso normal")
            print("Status: ESTÁ no peso ideal ✓")
        elif 25 <= imc < 30:
            print("Classificação: Sobrepeso")
            print("Status: NÃO está no peso ideal")
        else:
            print("Classificação: Obesidade")
            print("Status: NÃO está no peso ideal")

        print(f"\nReferência OMS - Peso ideal: IMC entre 18,5 e 24,9")


if __name__ == "__main__":
    exercicio = Exercicio6()
    exercicio.calcular_imc()