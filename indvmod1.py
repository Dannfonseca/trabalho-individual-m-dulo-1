import re

def inserir_dados():
    lista_candidatos = []
    while True:

        nome = input("Nome do candidato: ")
        if not re.match(r"^[a-zA-Záéíóúãõç ]+$", nome):
            print("Erro: O nome deve conter apenas letras")
            continue

        while True:
            try:
                entrevista = float(input("Nota da entrevista (0-10): "))
                if not 0 <= entrevista <= 10:
                    raise ValueError
                break
            except ValueError:
                print("Erro: A nota da entrevista deve ser um número entre 0 e 10.")

        while True:
            try:
                teste_teorico = float(input("Nota do teste teórico (0-10): "))
                if not 0 <= teste_teorico <= 10:
                    raise ValueError
                break
            except ValueError:
                print("Erro: A nota do teste teórico deve ser um número entre 0 e 10.")

        while True:
            try:
                teste_pratico = float(input("Nota do teste prático (0-10): "))
                if not 0 <= teste_pratico <= 10:
                    raise ValueError
                break
            except ValueError:
                print("Erro: A nota do teste prático deve ser um número entre 0 e 10.")

        while True:
            try:
                soft_skills = float(input("Nota de soft skills (0-10): "))
                if not 0 <= soft_skills <= 10:
                    raise ValueError
                break
            except ValueError:
                print("Erro: A nota de soft skills deve ser um número entre 0 e 10.")

        candidato = {
            "nome": nome,
            "entrevista": entrevista,
            "teste_teorico": teste_teorico,
            "teste_pratico": teste_pratico,
            "soft_skills": soft_skills,
        }
        lista_candidatos.append(candidato)

        continuar = input("Deseja inserir mais dados? (S/N) ")
        if not continuar.lower().startswith("s"):
            break

    return lista_candidatos

def exibir_resultados(lista_candidatos):
    for candidato in lista_candidatos:
        print("---------------------------------------------")
        print("Resultado")
        print("---------------------------------------------")
        print(f"Nome: {candidato['nome']}")
        print(f"Entrevista: {candidato['entrevista']}")
        print(f"Teste teórico: {candidato['teste_teorico']}")
        print(f"Teste prático: {candidato['teste_pratico']}")
        print(f"Soft skills: {candidato['soft_skills']}")

def buscar_por_nota(lista_candidatos):
    pesquisar = input("Você deseja pesquisar algum resultado? (S/N) ")
    if not pesquisar.lower().startswith("s"):
        return

    while True:
        try:
            valor_minimo = float(input("Digite a nota mínima desejada (0-10): "))
            if not 0 <= valor_minimo <= 10:
                raise ValueError
            break
        except ValueError:
            print("Erro: A nota mínima deve ser um número entre 0 e 10.")

    candidatos_encontrados = []
    for candidato in lista_candidatos:
        notas_atendidas = {}
        for chave, valor in candidato.items():
            if chave != "nome" and valor >= valor_minimo:
                notas_atendidas[chave] = valor
        if notas_atendidas:
            candidatos_encontrados.append({"nome": candidato["nome"], "notas": notas_atendidas})

    if candidatos_encontrados:
        print("---------------------------------------------")
        print(f"Resultados para nota mínima de {valor_minimo}")
        print("---------------------------------------------")
        for candidato in candidatos_encontrados:
            print(f"Nome: {candidato['nome']}")
            for materia, nota in candidato['notas'].items():
                print(f"{materia}: {nota}")
    else:
        print("Nenhum candidato encontrado com a nota mínima de", valor_minimo)

lista_candidatos = inserir_dados()
exibir_resultados(lista_candidatos)
buscar_por_nota(lista_candidatos)
