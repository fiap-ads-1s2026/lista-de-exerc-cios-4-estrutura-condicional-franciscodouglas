class Exercicio5:
    """Algoritmo que realiza verificação previdenciária"""
    
    def verificar_aposentadoria(self):
        idade = int(input("Digite a idade cronológica (anos): "))
        tempo_servico = int(input("Digite o tempo de contribuição (anos): "))

        if idade < 0 or tempo_servico < 0:
            print("ERRO: Idade e tempo de serviço devem ser valores positivos")
            return

        if tempo_servico > idade:
            print("ERRO: Tempo de serviço não pode ser maior que a idade")
            return

        print(f"\nDados do colaborador:")
        print(f"Idade: {idade} anos")
        print(f"Tempo de contribuição: {tempo_servico} anos")

        criterio_idade = idade >= 65
        criterio_tempo = tempo_servico >= 30
        criterio_misto = idade >= 60 and tempo_servico >= 25

        print(f"\nAnálise dos critérios:")
        print(f"• Critério por Idade (≥65 anos): {'✓ ATENDE' if criterio_idade else '✗ NÃO ATENDE'}")
        print(f"• Critério por Tempo (≥30 anos): {'✓ ATENDE' if criterio_tempo else '✗ NÃO ATENDE'}")
        print(f"• Critério Misto (≥60 anos + ≥25 anos serviço): {'✓ ATENDE' if criterio_misto else '✗ NÃO ATENDE'}")

        if criterio_idade or criterio_tempo or criterio_misto:
            print(f"\nPARECER: O trabalhador ESTÁ APTO para aposentadoria")
        else:
            print(f"\n PARECER: O trabalhador NÃO ESTÁ APTO para aposentadoria")
            print("\nPara se aposentar, é necessário atender pelo menos um dos critérios:")
            print(f"• Completar {65 - idade} anos (critério idade)")
            print(f"• Contribuir por mais {30 - tempo_servico} anos (critério tempo)")
            print(f"• Ou atingir {max(0, 60 - idade)} anos de idade e {max(0, 25 - tempo_servico)} anos de contribuição (critério misto)")


if __name__ == "__main__":
    exercicio = Exercicio5()
    exercicio.verificar_aposentadoria()