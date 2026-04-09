class Exercicio7:
    """Algoritmo que solicita a idade de um nadador e imprime sua categoria"""
    
    def categorizar_nadador(self):
        idade = int(input("Digite a idade do nadador: "))

        if idade < 0:
            print("ERRO: A idade deve ser um valor positivo")
            return

        print(f"\nIdade informada: {idade} anos")

        if idade < 5:
            print("Categoria: O atleta não possui categoria definida")
            print("Motivo: Idade inferior a 5 anos")
        elif 5 <= idade <= 10:
            print("Categoria: INFANTIL")
            print("Faixa etária: 5 a 10 anos")
        elif 11 <= idade <= 17:
            print("Categoria: JUVENIL")
            print("Faixa etária: 11 a 17 anos")
        else:
            print("Categoria: SÊNIOR")
            print("Faixa etária: 18 anos ou mais")


if __name__ == "__main__":
    exercicio = Exercicio7()
    exercicio.categorizar_nadador()