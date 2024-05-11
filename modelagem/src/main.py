import pandas as pd
from graphviz import Graph

def ler_excel(nome_arquivo, skip_rows, num_rows):
    """Carrega um arquivo Excel em um DataFrame."""
    df = pd.read_excel(nome_arquivo, skiprows=skip_rows, nrows=num_rows)
    df.drop(['Unnamed: 0', 'Unnamed: 1'], axis=1, inplace=True)
    return df

def obter_disciplinas(df):
    """Retorna a lista de disciplinas."""
    return list(df['SIGLA'])

def obter_professores(df):
    """Retorna a lista de professores, baseada nas colunas do DataFrame."""
    professores = [col for col in df.columns if 'prof' in col]
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
                relacoes.extend([(professor, sigla) for _ in range(int(linha[professor]))])
    return relacoes

if __name__ == "__main__":
    nome_arquivo = '../data/cenario6_dados.xlsx'
    df = ler_excel(nome_arquivo, skip_rows=7, num_rows=21)
    
    disciplinas = obter_disciplinas(df)
    professores = obter_professores(df)
    relacoes = obter_relacoes_prof_disciplina(df.set_index('SIGLA'), professores)
    
    dot = construir_grafo(disciplinas, professores, relacoes)
    dot.render('../output/output', view=False)
