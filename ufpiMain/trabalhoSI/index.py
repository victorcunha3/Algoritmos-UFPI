import random

def fazer_pergunta(pergunta, alternativas, resposta_correta):
    print(pergunta)
    for i, alternativa in enumerate(alternativas, start=1):
        print(f"{i}. {alternativa}")

    resposta = int(input("Escolha a alternativa correta (1, 2 ou 3): "))
    if resposta == resposta_correta:
        print("Resposta correta!\n")
        return 1
    else:
        print(f"Resposta incorreta. A resposta correta era a alternativa {resposta_correta}.\n")
        return 0

def main():
    perguntas = [
        #1
        {
            "pergunta": "O que é um Sistema de Informação?",
            "alternativas": ["Conjunto de componentes inter-relacionados que coleta (ou recupera), processa, armazena e distribui informação para dar suporte à tomada de decisão e ao controle da organização", 
                             "Um supercomputador", 
                             "São os chips que ficam alocados na máquina"],
            "resposta_correta": 1
        },
        #2
        {
            "pergunta": "O que são dados?",
            "alternativas": ["São sucessões de fatos brutos que não foram organizados, processados, relacionados, avaliados ou interpretados, representando apenas, partes isoladas de eventos, situações ou ocorrências",
                             "São sucessões de fatos brutos que não foram organizados, processados,  não relacionados, avaliados e não interpretados, representando apenas partes isoladas de eventos",
                             "Ambas as alternativas estão incorretas"],
            "resposta_correta": 1
        },
        #3
        {
            "pergunta": "Qual desses é um objetivo das SIs nas empresas?",
            "alternativas": ["Diminuir a excelência operacional",
                             "Melhorar a tomada de decisão",
                             "Promover a desvantagem competitiva"],
            "resposta_correta": 2
        },
        #4
        {
            "pergunta": "defina empresa:",
            "alternativas": ["organização formal cujo objetivo é produzir produtos ou prestar serviços a fim de gerar lucro",
                             "Organização que visa o prejuízo",
                             "Organização exclusiva para causas ambientais"],
            "resposta_correta": 1
        },
        #5
        {
            "pergunta": "defição de Metadados:",
            "alternativas": ["Eles fornecem informações sobre um recurso informacional, como sua criação, conteúdo, formato, localização, etc",
                             "são pequenos robôs que vivem dentro do seu computador e organizam seus arquivos automaticamente",
                             "Metadados são códigos secretos usados por agentes secretos para se comunicarem através de documentos digitais"],
            "resposta_correta": 1
        },
        #6
        {
            "pergunta": "O que são Banco de Dados?",
            "alternativas": ["Um banco de dados é um sistema organizado para coletar, armazenar e gerenciar dados. Ele fornece uma estrutura que permite a inserção, atualização, pesquisa e recuperação eficientes de informações",
                             "Um banco de dados é um depósito subterrâneo onde as organizações secretas guardam informações confidenciais",
                             "Um banco de dados é uma prateleira gigante em uma biblioteca que armazena livros e documentos físicos"],
            "resposta_correta": 1
        },
        #7
        {
            "pergunta": "O que é um Sistema ERP?",
            "alternativas": [
                            "Um sistema ERP é um dispositivo eletromagnético de realinhamento planetário usado para prever mudanças climáticas extremas.",
                             "Um sistema ERP é um grupo de especialistas em resolução de problemas que ajudam as empresas a superar desafios operacionais",
                             "é um software integrado que ajuda as organizações a gerenciar e automatizar processos empresariais, como contabilidade, compras, inventário, recursos humanos"],
            "resposta_correta": 3
        },
        #8
        {
            "pergunta": "Qual dos itens abaixo é um exemplo de Sistema de Gerenciamneto de Banco de Dados Relacional?",
            "alternativas": [
                            "MongoDB",
                             "CassandraDB",
                             "Postgress"],
            "resposta_correta": 3
        },
        #9
        {
            "pergunta": "Quantas fases possui um projeto ERP(Planejamento de Recursos Empresariais)?",
            "alternativas": [
                            "7",
                             "4",
                             "6"],
            "resposta_correta": 3
        },
        #10
        {
            "pergunta": "Qual dessas é uma desvantagem do ERP(Planejamento de Recursos Empresariais)?",
            "alternativas": [
                            "Implementação demorada",
                             "Evita trabalho duplicado",
                             "Diminui o tempo de entrega do produto"],
            "resposta_correta": 1
        },
        #11
        {
            "pergunta": "O que significa LGPD?",
            "alternativas": [
                            "Lei Geral da Proteção de Dados",
                             "Lei Geral da Diminuição de Dados",
                             "Lei Geral da Poluição de Dados"],
            "resposta_correta": 1
        },
        #12
        {
            "pergunta": "Qual dessas alternativas NÃO é um estilo de Tomada de Decisão?",
            "alternativas":["Estilo Analítico",
                            "Estilo Diretivo",
                            "Estilo Programado"],
            "respota_correta":3
        },
        #13
        {
            "pergunta": "Qual dessas alternativas NÃO se encaixa em um nível do processo de Sistemas de Apoio à decisão?",
            "alternativas":["Decisões Não Programadas",
                            "Decisões Programadas",
                            "Decisões Conceituadas"],
            "respota_correta":3
        },
        #14

        
    ]

    score = 0

    random.shuffle(perguntas)

    for perguntaAtual in perguntas[:20]:
        pergunta = perguntaAtual["pergunta"]
        alternativas = perguntaAtual["alternativas"]
        resposta_correta = perguntaAtual["resposta_correta"]

        score += fazer_pergunta(pergunta, alternativas, resposta_correta)

    print(f"Jogo encerrado! Seu score final é: {score}")

if __name__ == "__main__":
    main()
