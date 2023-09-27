# Importación, visualización, manipulación de datos
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from ydata_profiling import ProfileReport
# Transformación de datos
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report
# RNA
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping

# Visualización de resultados
from sklearn.metrics import confusion_matrix
# Lectura del dataset
dataset = pd.read_csv("players_15.csv")
"""columns_names = dataset.columns.values
#print(columns_names)
top_players = dataset.groupby("short_name")["power_shot_power"].sum()
print(top_players.sort_values(ascending=False).head(10))"""
# Más ejemplos de gráficas. Distribuciones respecto a la salida
for col in dataset.columns:
    plt.title(col)
    sns.histplot(data=dataset, x = col, hue='short_name')
    plt.show()
