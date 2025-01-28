# Quiz Habilitatorio: Regresión Lineal y Clustering con K-Means

---

## **Sección 1: Regresión Lineal**

### **Teoría (Responde Verdadero o Falso)**

1. La **regresión lineal simple** asume una relación lineal entre las variables independientes y dependientes.  
2. En la **regresión lineal múltiple**, un coeficiente de una variable independiente representa su influencia en la variable dependiente, manteniendo las demás variables constantes.  
3. Un valor de \(R^2\) alto siempre garantiza que el modelo de regresión sea válido.  
4. Si los residuos de un modelo de regresión lineal muestran un patrón sistemático, significa que las suposiciones del modelo se cumplen.  

### **Interpretación (Opción Múltiple)**

5. Tienes un modelo de regresión lineal con la ecuación:  
   \[
   y = 2.5 + 1.8x_1 - 0.5x_2
   \]  
   ¿Qué significa el coeficiente de \(x_2\)?  
   - a) Por cada incremento unitario en \(x_2\), \(y\) disminuye en promedio 0.5 unidades.  
   - b) Por cada incremento unitario en \(x_2\), \(y\) aumenta en promedio 0.5 unidades.  
   - c) Por cada incremento de 2.5 unidades en \(x_2\), \(y\) permanece constante.  
   - d) No tiene interpretación.  

6. Un modelo de regresión tiene un valor \(p\)-value para una variable independiente de 0.04. ¿Qué puedes concluir?  
   - a) La variable es estadísticamente significativa al nivel del 5%.  
   - b) La variable no es significativa porque el valor \(p > 0.01\).  
   - c) El valor \(p\) indica que el modelo tiene errores de multicolinealidad.  

### **Ejercicio Práctico**

7. Tienes los siguientes datos:  

| \(x\) | \(y\) |  
|------|------|  
| 1    | 2.5  |  
| 2    | 3.1  |  
| 3    | 4.2  |  
| 4    | 5.0  |  
| 5    | 6.1  |  

Ajusta un modelo de regresión lineal de la forma \(y = \beta_0 + \beta_1x\). Calcula manualmente los coeficientes \(\beta_0\) y \(\beta_1\) usando las fórmulas de mínimos cuadrados.  

---

## **Sección 2: Clustering con K-Means**

### **Teoría (Responde Verdadero o Falso)**

1. El algoritmo K-Means minimiza la suma de las distancias cuadradas de los puntos al centroide más cercano.  
2. Para determinar el número óptimo de clusters \(k\), es común usar el método del "codo".  
3. En K-Means, es necesario que los datos estén escalados antes de aplicar el algoritmo.  
4. K-Means puede garantizar encontrar el agrupamiento óptimo global en cada ejecución.  

### **Interpretación (Opción Múltiple)**

5. Ejecutas un K-Means con \(k=3\) y obtienes los siguientes resultados:  
   - Cluster 1: 50 puntos, promedio en la dimensión \(x=3.5\), \(y=7.2\).  
   - Cluster 2: 30 puntos, promedio en la dimensión \(x=8.1\), \(y=2.4\).  
   - Cluster 3: 20 puntos, promedio en la dimensión \(x=5.5\), \(y=4.6\).  

   ¿Cuál es una posible interpretación de estos clusters?  
   - a) Los datos están agrupados en regiones de características similares.  
   - b) Cada cluster tiene la misma cantidad de puntos.  
   - c) Los centroides son irrelevantes para interpretar los clusters.  
   - d) K-Means siempre genera clusters esféricos, lo cual se cumple aquí.  

### **Ejercicio Práctico**

6. Tienes el siguiente conjunto de datos en dos dimensiones:  

| \(x_1\) | \(x_2\) |  
|--------|--------|  
| 1.0    | 2.0    |  
| 1.5    | 1.8    |  
| 5.0    | 8.0    |  
| 8.0    | 8.0    |  
| 1.0    | 0.6    |  
| 9.0    | 11.0   |  
| 8.0    | 2.0    |  
| 10.0   | 2.0    |  

Aplica el algoritmo K-Means con \(k=2\). Calcula manualmente las posiciones iniciales de los centroides, asigna los puntos a los clusters y recalcula los centroides tras una iteración.  

---

## **Resultados**

1. Corrige las preguntas teóricas.  
2. Interpreta los ejercicios prácticos, incluyendo si los resultados son consistentes con las expectativas.  
