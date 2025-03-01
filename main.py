import os
import pandas as pd
from utils.data_functions import *

# Exemplo de uso
data_folder = 'data'
output_folder = os.path.join(data_folder, 'aglomerado')
aglomerar_resultados(data_folder, output_folder)

# Gerar relatório para uma turma específica
file_path = os.path.join(output_folder, 'turma_5D.xlsx')

resultado_turma(file_path)

for filename in os.listdir(output_folder):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(output_folder, filename)
        resultado_turma(file_path)
