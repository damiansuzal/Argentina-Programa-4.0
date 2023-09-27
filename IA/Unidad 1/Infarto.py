# Importación, visualización, manipulación de datos
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from zipfile import ZipFile
from torch.utils.data import Dataset

# Transformación de datos
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

"""test_file_name = "ataques_corazon.zip"

# descomprime el archivo ZIP
with ZipFile(test_file_name, 'r') as zip:
    zip.printdir()
    zip.extractall() """

# Lectura del dataset
dataset = pd.read_csv("ataques_corazon.csv")
# Para visualizar un fragmento de los datos
dataset.head(5)
dataset.info()

# Ejemplo de gráfica para una idea de las distribuciones
dataset['class'].value_counts().plot.pie()
# Mostrar los gráficos pie en una ventana emergente
plt.show()

# Mapa de correlaciones, se puede observar dependencias entre columnas. Permite descartar descriptores que no 
# aportan información nueva por ejemplo (resta costo computacional, etc.)
# Antes de plantear cualquier modelo, existe un gran trabajo de procesamiento y análisis de los datos. 
# Herramientas Estadísticas juegan un roll fundamental.

numeric_features = dataset.select_dtypes(include=[np.number])
sns.heatmap(data=numeric_features.corr(), annot=True)
plt.show()

fig=plt.gcf()
fig.set_size_inches(10,6)
plt.show()

# En este caso, por ejemplo, no se observan fuertes relaciones entre las variables. Por lo tanto, 
# en principio existe información útil en todas.
# NOTA: variables aletorias tampoco estarán correlacionadas, pero en este punto, asumimos que anteriormente 
# validamos que estas variables "tienen que ver" con nuestro problema.

# Más ejemplos de gráficas. Distribuciones respecto a la salida
for col in dataset.columns:
    plt.title(col)
    sns.histplot(data=dataset, x = col, hue='class')
    plt.show()

# Se aprecia por ejemplo, que existen superposiciones en los rangos de las variables. 
# Por lo tanto, no sería tan sencillo clasificar las clases de salida
# y obtener una precisión buena con simples secuencias de selección (IF anidados por ejemplo, 
# en dónde se establece un umbral estricto).

# Tratamiento de los datos y división del dataset
# Definición de la columna de salida esperada (aprendizaje supervisado)
y = dataset.pop('class')
print("Y antes:\n", y[:5])

# Preprocesamiento
# Se codifica numéricamente las categorías definidas con etiquetas. 
# Ej.: en lugar de “Joven” y “Adulto” en la clase, queda 0 y 1.
le = LabelEncoder()

y = le.fit_transform(y)     # Con le.inverse_transform() recuperamos luego la etiqueta original
print("Y despues: ", y[:5])