class Exercicio3:
    """Algoritmo que calcula o desempenho acadêmico com média ponderada"""
    
    def calcular_desempenho_academico(self):
        nota1 = float(input("Digite a nota da primeira avaliação (peso 1): "))
        nota2 = float(input("Digite a nota da segunda avaliação (peso 1): "))
        nota3 = float(input("Digite a nota da terceira avaliação (peso 2): "))

        if not all(0 <= nota <= 10 for nota in [nota1, nota2, nota3]):
            print("ERRO: As notas devem estar entre 0 e 10")
            return

        media_final = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

        print(f"\nNotas das avaliações:")
        print(f"1ª avaliação (peso 1): {nota1:.1f}")
        print(f"2ª avaliação (peso 1): {nota2:.1f}")
        print(f"3ª avaliação (peso 2): {nota3:.1f}")
        print(f"\nMédia final: {media_final:.1f}")

        if media_final >= 6.0:
            print("Status: APROVADO")
        else:
            print("Status: REPROVADO")


if __name__ == "__main__":
    exercicio = Exercicio3()
    exercicio.calcular_desempenho_academico()