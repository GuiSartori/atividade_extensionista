import os
import pandas as pd
from openpyxl import load_workbook
'''
def aglomerar_resultados(data_folder, output_folder):
    # Verificar se a pasta de saída existe, se não, criar
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Dicionário para armazenar DataFrames por turma
    turmas = {}
    
    # Iterar pelos arquivos na pasta de dados
    raw_folder = os.path.join(data_folder, 'raw')
    for filename in os.listdir(raw_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(raw_folder, filename)
            # Ler o arquivo CSV
            df = pd.read_csv(file_path)
            
            # Obter a turma a partir do nome do arquivo
            turma = filename.split('_')[-1].replace('.csv', '')
            
            # Adicionar o DataFrame ao dicionário de turmas
            if turma not in turmas:
                turmas[turma] = []
            turmas[turma].append(df)
    
    # Combinar os DataFrames de cada turma e adicionar o gabarito
    gabarito = ["Gabarito", "B", "A", "B", "B", "B"]
    for turma, dfs in turmas.items():
        gabarito_df = pd.DataFrame([gabarito], columns=dfs[0].columns)
        combined_df = pd.concat([gabarito_df] + dfs, ignore_index=True)
        output_file = os.path.join(output_folder, f"turma_{turma}.xlsx")
        combined_df.to_excel(output_file, index=False)

def resultado_turma(file_path):
    df = pd.read_excel(file_path)
    
    # Separar o gabarito dos resultados
    gabarito = df.iloc[0, 1:].values
    resultados = df.iloc[1:].copy()
    
    # Contar os acertos por questão
    questoes = ["Questao 1", "Questao 2", "Questao 3", "Questao 4", "Questao 5"]
    acertos = {questao: 0 for questao in questoes}
    
    for questao in questoes:
        acertos[questao] = (resultados[questao] == gabarito[questoes.index(questao)]).sum()
    
    # Calcular a porcentagem de acertos
    porcentagem_acertos = {questao: 0 for questao in questoes}
    total_alunos = len(resultados)
    
    for questao in questoes:
        porcentagem_acertos[questao] = acertos[questao] / total_alunos * 100
    
    # Criar um DataFrame com o relatório
    relatorio_df = pd.DataFrame({
        "Questao": questoes,
        "Acertos": [acertos[questao] for questao in questoes],
        "Porcentagem de Acertos (%)": [porcentagem_acertos[questao] for questao in questoes]
    })
    
    # Salvar o relatório em um novo arquivo Excel
    relatorio_file = file_path.replace(".xlsx", "_relatorio.xlsx")
    with pd.ExcelWriter(relatorio_file, engine='openpyxl') as writer:
        relatorio_df.to_excel(writer, sheet_name="Relatorio", index=False)
        df.to_excel(writer, sheet_name="Dados Aglomerados", index=False)

'''

import os
import pandas as pd
from openpyxl import load_workbook

def aglomerar_resultados(data_folder, output_folder):
    # Verificar se a pasta de saída existe, se não, criar
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Dicionário para armazenar DataFrames por turma
    turmas = {}
    
    # Iterar pelos arquivos na pasta de dados
    raw_folder = os.path.join(data_folder, 'raw')
    for filename in os.listdir(raw_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(raw_folder, filename)
            # Ler o arquivo CSV
            df = pd.read_csv(file_path)
            
            # Obter a turma a partir do nome do arquivo
            turma = filename.split('_')[-1].replace('.csv', '')
            
            # Adicionar o DataFrame ao dicionário de turmas
            if turma not in turmas:
                turmas[turma] = []
            turmas[turma].append(df)
    
    # Combinar os DataFrames de cada turma e adicionar o gabarito
    gabarito = ["Gabarito", "B", "A", "B", "B", "B"]
    for turma, dfs in turmas.items():
        gabarito_df = pd.DataFrame([gabarito], columns=dfs[0].columns)
        combined_df = pd.concat([gabarito_df] + dfs, ignore_index=True)
        output_file = os.path.join(output_folder, f"turma_{turma}.xlsx")
        combined_df.to_excel(output_file, index=False)

def resultado_turma(file_path):
    df = pd.read_excel(file_path)
    
    # Separar o gabarito dos resultados
    gabarito = df.iloc[0, 1:].values
    resultados = df.iloc[1:].copy()
    
    # Contar os acertos por questão
    questoes = ["Questao 1", "Questao 2", "Questao 3", "Questao 4", "Questao 5"]
    acertos = {questao: 0 for questao in questoes}
    
    for questao in questoes:
        acertos[questao] = (resultados[questao] == gabarito[questoes.index(questao)]).sum()
    
    # Calcular a porcentagem de acertos
    porcentagem_acertos = {questao: 0 for questao in questoes}
    total_alunos = len(resultados)
    
    for questao in questoes:
        porcentagem_acertos[questao] = acertos[questao] / total_alunos * 100
    
    # Criar um DataFrame com o relatório
    relatorio_df = pd.DataFrame({
        "Questao": questoes,
        "Acertos": [acertos[questao] for questao in questoes],
        "Porcentagem de Acertos (%)": [porcentagem_acertos[questao] for questao in questoes]
    })
    
    # Salvar o relatório em um novo arquivo Excel
    relatorio_file = file_path.replace(".xlsx", "_relatorio.xlsx")
    with pd.ExcelWriter(relatorio_file, engine='openpyxl') as writer:
        relatorio_df.to_excel(writer, sheet_name="Relatorio", index=False)
        df.to_excel(writer, sheet_name="Dados Aglomerados", index=False)
