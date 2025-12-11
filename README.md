# Trabajo-Final-Lenguajes

Este proyecto integra análisis de datos y desarrollo de una mini-API, siguiendo los requisitos del Trabajo Práctico Final. El objetivo principal fue analizar el dataset “TMDB 5000 Movies” y exponer los resultados mediante una API capaz de entregar la información procesada a cualquier usuario o aplicación.
Explicación general del proyecto y su conexión con la mini-API

Este proyecto tiene dos partes integradas:
	1.	un análisis de datos completo realizado en un Jupyter Notebook, y
	2.	una mini-API desarrollada con FastAPI que expone los resultados obtenidos en ese análisis.

# Análisis de datos (Notebook)

En el notebook se llevó a cabo todo el procesamiento del dataset TMDB 5000 Movies:

	•	Lectura de los archivos CSV originales.
	
	•	Limpieza y preparación de datos (fechas, columnas JSON, valores nulos, filtrado de películas válidas).
	
	•	Cálculo de métricas necesarias para responder los tres ejes del trabajo:
	
	•	Rentabilidad por género y país (ROI).
	
	•	Relación entre presupuesto y rating.
	
	•	Evolución de la duración de películas.
	
	•	EGeneración de gráficos y estadísticas descriptivas para responder a cada eje.
	
	•	Exportación de los resultados procesados a la carpeta artifacts/ en formato JSON y CSV.
  
En esta primera parte sucede toda la lógica y todo el procesamiento del proyecto.

# Conexión con la mini-API

La segunda parte del proyecto consiste en una mini-API desarrollada en FastAPI cuyo propósito es: 

Exponer los resultados ya procesados en el notebook, para que puedan ser consultados por cualquier usuario o aplicación.

Es importante remarcar que:
	•	La API no realiza cálculos ni análisis.
	•	Solo lee los archivos JSON/CSV generados previamente y los devuelve en distintos endpoints.

La API se organiza dentro de la carpeta services/, cada archivo cumple un rol específico:

	•	roi_service.py -> carga los datos de ROI por género y por país.
	
	•	runtime_service.py -> carga la evolución de la duración de las películas.
	
	•	correlation_service.py -> carga la correlación presupuesto-rating.
  
El archivo main.py:

	•	crea la aplicación FastAPI
	
	•	define los endpoints
	
	•	Y utiliza los servicios anteriores para retornar los datos.

Así, la API actúa como una capa de acceso a los resultados producidos en el notebook

# Relación entre ambas partes

El flujo del proyecto es:

	1.	El notebook procesa los datos.
	
	2.	Genera archivos JSON/CSV en /artifacts/.
	
	3.	La mini-API lee esos archivos y los expone.

De esta manera:

	•	El análisis y el procesamiento pertenecen al Notebook.
	
	•	La API funciona como un medio de acceso a esos análisis.
	
	•	Ambas partes están conectadas y cumplen con los requisitos del Trabajo Final.
