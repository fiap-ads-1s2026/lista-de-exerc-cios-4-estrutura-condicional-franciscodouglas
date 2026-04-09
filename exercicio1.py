class Exercicio1:
    """Algoritmo que receba duas notas escolares e calcule a média aritmética"""
    
    def calcular_media_notas(self):
        nota1 = float(input("Digite a primeira nota (0.0 a 10.0): "))
        nota2 = float(input("Digite a segunda nota (0.0 a 10.0): "))

        if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
            print("ERRO: As notas devem estar no intervalo de 0.0 a 10.0")
            return

        media = (nota1 + nota2) / 2

        print(f"Nota 1: {nota1:.1f}")
        print(f"Nota 2: {nota2:.1f}")
        print(f"Média aritmética: {media:.1f}")


if __name__ == "__main__":
    exercicio = Exercicio1()
    exercicio.calcular_media_notas()