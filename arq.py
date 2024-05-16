import pandas as pd

# Criando um DataFrame de exemplo
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']}

df = pd.DataFrame(data)

# Exibindo o DataFrame original
print("DataFrame original:")
print(df)

# Adicionando uma nova coluna ao DataFrame
df['Profissão'] = ['Engenheira', 'Advogado', 'Professor', 'Médico']

# Exibindo o DataFrame com a nova coluna
print("\nDataFrame com a nova coluna 'Profissão':")
print(df)
