# Study.Track
StudyTracker es un proyecto desarrollado en Python para ayudar a estudiantes a organizar sus notas y evaluaciones. Incluye los principales ramos del sistema escolar chileno y utiliza su escala de calificaciones.
## FUNCIONALIDADES
Permite agregar, editar, eliminar y consultar notas organizadas por ramo, además de calcular sus promedios. También permite gestionar evaluaciones y consultar las próximas pruebas de las siguientes dos semanas.
Cuenta con un resumen académico que muestra el promedio, la nota mínima y la nota máxima de cada ramo, además del promedio general y los ramos con mayor y menor promedio.
## Guardado de datos
Las notas y evaluaciones se guardan en archivos JSON, lo que permite conservar los datos entre sesiones y recuperarlos al volver a abrir el programa.
## Cómo ejecutarlo
Probado con Python 3.14.7. 
1. Abrir el archivo StudyTracker.py y abrir directamente con el editor de IDLE.
2. Para ejecutar el programa se debe pulsar F5 en el IDLE. 
## Limitaciones
Utiliza el menú de consola para interactuar, no tiene interfaz gráfica. El guardado en JSON no sincroniza por sí mismo la información entre dispositivos ni constituye una copia de seguridad. Los ramos y la escala de notas están adaptados al contexto escolar chileno. Presenta promedios, mínimos y máximos; todavía no incluye gráficos ni medidas de dispersión. 
## Mejoras previstas para V4
- Incorporar los gráficos de evolución y la línea de tendencia.
- Añadir varianza y desviación estándar al análisis.
