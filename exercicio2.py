class Exercicio2:
    """Algoritmo que analisa a viabilidade de um crédito financeiro"""
    
    def analisar_credito(self):
        salario_bruto = float(input("Digite o salário bruto (R$): "))
        valor_parcela = float(input("Digite o valor mensal da parcela desejada (R$): "))

        if salario_bruto <= 0 or valor_parcela <= 0:
            print("ERRO: Os valores devem ser maiores que zero")
            return

        percentual_comprometimento = (valor_parcela / salario_bruto) * 100

        print(f"Salário bruto: R$ {salario_bruto:.2f}")
        print(f"Valor da parcela: R$ {valor_parcela:.2f}")
        print(f"Comprometimento de renda: {percentual_comprometimento:.1f}%")

        if percentual_comprometimento > 20:
            print("\nSOLICITAÇÃO NEGADA: A prestação excede 20% do salário")
        else:
            print("\nSOLICITAÇÃO APROVADA: O valor está dentro do limite permitido")


if __name__ == "__main__":
    exercicio = Exercicio2()
    exercicio.analisar_credito()