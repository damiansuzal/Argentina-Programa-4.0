from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC  # Como ejemplo de modelo
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt # Visualización de datos
import pandas as pd # Resumen estadístico

# Cargamos un conjunto de datos de ejemplo (por ejemplo, Iris)
data = load_iris()
X = data.data  # Las características se almacenan en X
y = data.target  # Las etiquetas se almacenan en y

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf", "poly"],
    "gamma": [0.1, 1, "scale", "auto"]
}
grid_search = GridSearchCV(estimator=SVC(), param_grid=param_grid, scoring="accuracy", cv=5)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
"""
# Visualizar un histograma de una columna de datos
plt.hist(data["columna"])
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Histograma de Datos")
plt.show()

# Crear un DataFrame de ejemplo
data = pd.DataFrame({'columna': [1, 2, 3, 4, 5]})

# Acceder a la columna 'nombre_columna'
columna = data['columna']
print(columna)

# Visualizar un histograma de una columna de datos
plt.hist(columna)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Datos')
plt.show()"""
"""
# Calcular estadísticas descriptivas
summary_stats = data.describe()
print(summary_stats)"""
df=data
df.head(5)
df.info()
print("")
print("Esto es X: ",X)
print("Esto es Y: ",y)
print("Accuracy:", accuracy)
