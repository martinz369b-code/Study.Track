# Study.Track
StudyTracker es un proyecto desarrollado en Python para ayudar a estudiantes a organizar sus notas y evaluaciones. Incluye los principales ramos del sistema escolar chileno y utiliza su escala de calificaciones.
## FUNCIONALIDADES
Permite agregar, editar, eliminar y consultar notas organizadas por ramo, además de calcular sus promedios. También permite gestionar evaluaciones y consultar las próximas pruebas de las siguientes dos semanas.
Cuenta con un resumen académico que muestra el promedio, la nota mínima y la nota máxima de cada ramo, además del promedio general y los ramos con mayor y menor promedio.
## Guardado de datos
Las notas y evaluaciones se guardan en archivos JSON, lo que permite conservar los datos entre sesiones y recuperarlos al volver a abrir el programa.
## Cómo ejecutarlo
Probado con Python 3.14.7 y la biblioteca Matplotlib para generar los gráficos. 
1. Instalar Matplotlib en el entorno de Python utilizado para ejecutar el programa.
2. Descargar el archivo StudyTracker.py.
3. Abrirlo con el editor de IDLE.
4. Pulsar F5 para ejecutarlo.
## Limitaciones
Utiliza el menú de consola para interactuar, no tiene interfaz gráfica. El guardado en JSON no sincroniza por sí mismo la información entre dispositivos ni constituye una copia de seguridad. Los ramos y la escala de notas están adaptados al contexto escolar chileno. La tendencia describe las notas registradas, no garantiza resultados futuros. Una pendiente cero tampoco significa que todas las notas sean iguales.
## Novedades de  V4
- Gráficos de evolución de notas por ramo, con con linea que representa el promedio.
- Línea de tendencia para ramos con al menos dos notas.
- Clasificación de la tendencia en el resumen académico: ascendente, descendente o sin tendencia lineal. Cuando faltan notas, se indica que los datos son insuficientes.
- Corrección de la validación de fechas para volver a solicitar una fecha cuando la ingresada no es válida.
