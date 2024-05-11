import pandas as pd
from graphviz import Graph


def ler_excel(nome_arquivo, skip_rows, num_rows):
    """Carrega um arquivo Excel em um DataFrame."""
    df = pd.read_excel(nome_arquivo, skiprows=skip_rows, nrows=num_rows)
    df.drop(
        ["Unnamed: 0", "Unnamed: 1", "PPC", "DISCIPLINA", "CH"], axis=1, inplace=True
    )
    return df


def obter_disciplinas(df):
    """Retorna a lista de disciplinas."""
    return list(df["SIGLA"])


def obter_professores(df):
    """Retorna a lista de professores, baseada nas colunas do DataFrame."""
    professores = [col for col in df.columns if "prof" in col]
    return professores


def construir_grafo(disciplinas, professores, relacoes):
    """Constrói um grafo com disciplinas, professores e suas relações."""
    dot = Graph()
    for disciplina in disciplinas:
        dot.node(disciplina, disciplina)
    for professor in professores:
        dot.node(professor, professor)
    dot.edges(relacoes)
    return dot


def obter_relacoes_prof_disciplina(df, professores):
    """Gera as relações entre professores e disciplinas."""
    relacoes = []
    for sigla, linha in df.iterrows():
        for professor in professores:
            if pd.notna(linha[professor]):
                relacoes.extend(
                    [(professor, sigla) for _ in range(int(linha[professor]))]
                )
    return relacoes


def dados(nome_arquivo, skiprows, numrows, droprows):
    """Coleta os dados necessarios no DataFrame para renderizar o grafo."""
    df = ler_excel(nome_arquivo, skip_rows=skiprows, num_rows=numrows)
    # Remove linhas apontadas na lista se o valor não for -99
    if droprows[0] != -99:
        df.drop(range(droprows[0], droprows[1]), inplace=True)
    adicionar_TAG(df)
    print(df)
    disciplinas = obter_disciplinas(df)
    professores = obter_professores(df)
    relacoes = obter_relacoes_prof_disciplina(df.set_index("SIGLA"), professores)
    dados = {
        "disciplinas": disciplinas,
        "professores": professores,
        "relacoes": relacoes,
    }
    return dados


def adicionar_TAG(df):
    """Adiciona as TAGs de CURSO e PERIODO para as respectivas SIGLAs."""
    # Cria a tag baseada na coluna "CURSO" (constante para todas as linhas)
    tag_curso = f'[{df["CURSO"].iloc[0]}]'
    # Atualiza todos os valores da coluna "SIGLA" adicionando as duas tags diretamente
    df["SIGLA"] = df["SIGLA"] + tag_curso + "[" + df["PER."].astype(str) + "]"
    # Descarta coluna PER. e CURSO
    df.drop("PER.", axis=1, inplace=True)
    df.drop("CURSO", axis=1, inplace=True)


def compilar_dados(cco, sin, opt, pos):
    """Reune todos os dados referentes a um semestre em uma só dict."""
    dados_2024_semestre = {
        "disciplinas": list(
            set(cco["disciplinas"]).union(
                set(sin["disciplinas"])
                .union(opt["disciplinas"])
                .union(pos["disciplinas"])
            )
        ),
        "professores": list(
            set(cco["professores"]).union(
                set(sin["professores"])
                .union(opt["professores"])
                .union(pos["professores"])
            )
        ),
        "relacoes": cco["relacoes"]
        + sin["relacoes"]
        + opt["relacoes"]
        + pos["relacoes"],
    }
    return dados_2024_semestre


if __name__ == "__main__":
    nome_arquivo = "../data/cenario6_dados.xlsx"
    # GRAFO REFERENTE AO PRIMEIRO SEMESTRE DE 2024
    semestre1_index = 7
    dados_cco1 = dados(
        nome_arquivo, skiprows=semestre1_index, numrows=21, droprows=[-99, -99]
    )
    dados_sin1 = dados(
        nome_arquivo, skiprows=semestre1_index, numrows=40, droprows=[0, 21]
    )
    dados_opt1 = dados(
        nome_arquivo, skiprows=semestre1_index, numrows=47, droprows=[0, 40]
    )
    dados_pos1 = dados(
        nome_arquivo, skiprows=semestre1_index, numrows=48, droprows=[0, 47]
    )
    dados_2024_1 = compilar_dados(dados_cco1, dados_sin1, dados_opt1, dados_pos1)
    dot = construir_grafo(
        dados_2024_1["disciplinas"],
        dados_2024_1["professores"],
        dados_2024_1["relacoes"],
    )
    dot.render("../output/output_2024_1", view=False)
    # GRAFO REFERENTE AO SEGUNDO SEMESTRE DE 2024
    semestre2_index = 59
    dados_cco2 = dados(
        nome_arquivo, skiprows=semestre2_index, numrows=13, droprows=[-99, -99]
    )
    dados_sin2 = dados(
        nome_arquivo, skiprows=semestre2_index, numrows=31, droprows=[0, 13]
    )
    dados_opt2 = dados(
        nome_arquivo, skiprows=semestre2_index, numrows=38, droprows=[0, 31]
    )
    dados_pos2 = dados(
        nome_arquivo, skiprows=semestre2_index, numrows=40, droprows=[0, 38]
    )
    dados_2024_2 = compilar_dados(dados_cco2, dados_sin2, dados_opt2, dados_pos2)
    dot = construir_grafo(
        dados_2024_2["disciplinas"],
        dados_2024_2["professores"],
        dados_2024_2["relacoes"],
    )
    dot.render("../output/output_2024_2", view=False)
