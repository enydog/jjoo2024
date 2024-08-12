import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Cargar el archivo CSV
file_path = 'Athletes.csv'
df = pd.read_csv(file_path)

# Convertir birth_date a formato datetime
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')

# Calcular la edad en base a birth_date
df['age'] = df['birth_date'].apply(lambda x: (datetime.today() - x).days // 365 if pd.notnull(x) else None)

# Disciplinas seleccionadas para el filtro
filtered_disciplines = [
    "['Cycling BMX Freestyle']",
    "['Cycling Road']",
    "['Cycling Mountain Bike']",
    "['Swimming']",
    "['Triathlon']",
    "['Breaking']",
    "['Skateboarding']",
    "['Surfing']",
    "['Athletics']"
]

# Filtrar el DataFrame para incluir solo las disciplinas seleccionadas
filtered_df = df[df['disciplines'].isin(filtered_disciplines)]

# Crear un gráfico de violín con orientación vertical para las disciplinas filtradas
plt.figure(figsize=(8, 12))
sns.violinplot(y='disciplines', x='age', data=filtered_df, inner='quartile')

# Configuración del gráfico
plt.title('Distribution of Ages for Selected Disciplines')
plt.ylabel('Disciplines')
plt.xlabel('Age')
plt.show()
