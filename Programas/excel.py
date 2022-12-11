import pandas as pd


alunos = {
    'nome': ['Italo', 'vinicius', 'tallys', 'lucas'],
    'sexo': ['M', 'M', 'F','M'],
    'idade': ['24', '19', '19', '23'],
    }

dataframe = pd.DataFrame(alunos)
dataframe.to_excel('./alunos.xlsx')