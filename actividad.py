import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
import os

# Verificar la existencia del archivo antes de cargarlo
file_path = './actividad2.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo no se encontró en la ruta especificada: {file_path}")

# 1. Carga de datos
data = pd.read_csv(file_path)

# 2. Conversión de variables categóricas
data['gender'] = data['gender'].map({'f': 'Femenino', 'm': 'Masculino'})
data['city_name'] = data['city_name'].astype('category')
data['department_name'] = data['department_name'].astype('category')
data['medicine_type'] = data['medicine_type'].astype('category')

# 3. Cálculo de medias por género
mean_pressures = data.groupby('gender')[['systolic_pressure', 'diastolic_pressure']].mean()
print("Medias de presión por género:")
print(mean_pressures)

# 4. Gráficos de boxplot
plt.figure(figsize=(12, 6))

# Boxplot presión sistólica
plt.subplot(1, 2, 1)
sns.boxplot(x='gender', y='systolic_pressure', data=data)
plt.title('Distribución de presión sistólica por género')
plt.ylabel('Presión sistólica')
plt.xlabel('Género')

# Boxplot presión diastólica
plt.subplot(1, 2, 2)
sns.boxplot(x='gender', y='diastolic_pressure', data=data)
plt.title('Distribución de presión diastólica por género')
plt.ylabel('Presión diastólica')
plt.xlabel('Género')

plt.tight_layout()
plt.show()

# 5. Histogramas de presiones
plt.figure(figsize=(12, 6))

# Histograma presión sistólica
plt.subplot(1, 2, 1)
sns.histplot(data['systolic_pressure'], bins=20, kde=True, color='blue')
plt.title('Histograma de presión sistólica')
plt.xlabel('Presión sistólica')
plt.ylabel('Frecuencia')

# Histograma presión diastólica
plt.subplot(1, 2, 2)
sns.histplot(data['diastolic_pressure'], bins=20, kde=True, color='green')
plt.title('Histograma de presión diastólica')
plt.xlabel('Presión diastólica')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# 6. Gráfico de dispersión usando seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='systolic_pressure', 
    y='diastolic_pressure', 
    hue='gender', 
    size='medicine_quantity', 
    data=data
)
plt.title('Dispersión de presión sistólica vs. presión diastólica')
plt.xlabel('Presión sistólica')
plt.ylabel('Presión diastólica')
plt.legend(title='Género')
plt.show()

# 7. Análisis ANOVA
anova_result = f_oneway(
    data[data['gender'] == 'Femenino']['systolic_pressure'],
    data[data['gender'] == 'Masculino']['systolic_pressure']
)

print("\nResultados del ANOVA para presión sistólica entre géneros:")
print(f"Estadístico F: {anova_result.statistic:.2f}")
print(f"Valor p: {anova_result.pvalue:.4f}")

anova_result_diastolic = f_oneway(
    data[data['gender'] == 'Femenino']['diastolic_pressure'],
    data[data['gender'] == 'Masculino']['diastolic_pressure']
)

print("\nResultados del ANOVA para presión diastólica entre géneros:")
print(f"Estadístico F: {anova_result_diastolic.statistic:.2f}")
print(f"Valor p: {anova_result_diastolic.pvalue:.4f}")

# 8. Gráfico de barras para medicamentos por departamento y género
plt.figure(figsize=(14, 8))

grouped_data = data.groupby(['department_name', 'gender'])['medicine_quantity'].sum().unstack()
grouped_data.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('Cantidad de medicamentos entregados por departamento y género')
plt.ylabel('Cantidad de medicamentos')
plt.xlabel('Departamento')
plt.legend(title='Género')
plt.tight_layout()
plt.show()

print("\nAnálisis completado.")
