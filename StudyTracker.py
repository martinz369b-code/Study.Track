import json
from datetime import datetime
import matplotlib.pyplot as plt
ARCHIVO = "notss.json"
ARCHIVO_EVA = "evaluaciones.json"
tipsos = ["Prueba", "Lectura", "Trabajo", "Proceso"]
estd = ["Pendiente", "Preparada", "Evaluada"]
evas = []
campo = ["ramo", "nombre", "fecha", "tipo", "prioridad", "estado"]
nombres_ramos = {
    "mtm": "Matemática",
    "lng": "Lenguaje",
    "hst": "Historia",
    "ing": "Inglés",
    "fsc": "Física",
    "qmc": "Química",
    "blg": "Biología"
}
def agregar_notas(ramos):
    ingresado = False
    ramo = ""
    while not ingresado:
        if ramo == "":
                ramo = input("¿A qué ramo quieres agregar nota? ")
        if ramo == "0":
            return
        if ramo in ramos:
            try:
                nota = float(input("¿Cuál es la nota que quieres agregar? "))
            except ValueError:
                print("Ingresa números")
                continue
            if nota == 0:
                return
            if nota < 1.0 or nota > 7.0:
                print("Ingresa una nota")
            else:
                ramos[ramo].append(nota)
                guardar_notas(ramos)
                ingresado = True
        else:
            print("Ingresa un ramo existente")
            ramo = ""
            guardar_notas(ramos)
def ver_notas(ramos):
    print("")
    print(" === NOTAS POR RAMO === ")
    print("")
    print(f'{"RAMO":<12} | {"NOTAS":<25} | {"PROMEDIO":<8}')
    print("-" * 52)

    for ramo in ramos:
        if len(ramos[ramo]) > 0:
            notas_txt = ", ".join(str(n) for n in ramos[ramo])
            promedio = sum(ramos[ramo]) / len(ramos[ramo])

            print(
                f'{nombres_ramos[ramo]:<12} | {notas_txt:<25} | {promedio:<4.1f}')

        else:
            print(
                f'{nombres_ramos[ramo]:<12} | {"—":<25} | '
                f'—'
            )
def ver_promedio_de_un_ramo(ramos):
    promedio = 0
    ramo = ""
    ingresado = False
    while not ingresado:
        if ramo == "":
                ramo = input("¿A qué ramo quieres ver el promedio?")
        if ramo == "0":
            return
        if ramo in ramos and len(ramos[ramo]) != 0:
            mini = ramos[ramo][0]
            maxi = ramos[ramo][0]
            for c in ramos[ramo]:
                promedio = promedio + c
                if c < mini:
                    mini = c
                if c > maxi:
                    maxi = c
            promedio = promedio / len(ramos[ramo])
            print("Tu promedio es", promedio)
            print("Nota máxima es", maxi)
            print("Nota mínima es", mini)
            ingresado = True
        elif ramo in ramos:
            print("Ese ramo no tiene notas")
            ramo = ""
        else:
            print("Ingresa un ramo existente")
            ramo = ""
def ver_resumen_general(ramos):
    print("")
    print("=== RESUMEN ACADÉMICO ===")
    print("")
    r = 0
    for c in ramos:
        if len(ramos[c]) != 0:
            r = 1
    if r != 0:
        print(f'{"RAMO":<12} | {"MÍNIMA":<6} | {"MÁXIMA":<6} | {"PROMEDIO":<8} | {"Tendencia":<10}')
        print("-" * 53)
    sin_notas = []
    maxia = ""
    minia = ""
    promgn = 0
    promg = 0
    for ramo in ramos:
        if len(ramos[ramo]) > 0:
            mini = min(ramos[ramo])
            maxi = max(ramos[ramo])
            prom = sum(ramos[ramo]) / len(ramos[ramo])
            tend = interpretar_tendencia(ramo)
            print(f'{nombres_ramos[ramo]:<12} | {mini:<6.1f} | {maxi:<6.1f} | {prom:<8.2f} | {tend:<8}')
            if minia == "":
                minia = prom
                minin = nombres_ramos[ramo]
            if maxia == "":
                maxia = prom
                maxin = nombres_ramos[ramo]
            promg = promg + prom
            promgn = promgn + 1
            if minia > prom:
                minia = prom
                minin = nombres_ramos[ramo]
            if maxia < prom:
                maxia = prom
                maxin = nombres_ramos[ramo]
        else:
            sin_notas.append(nombres_ramos[ramo])
    if promg != 0:
        prom = promg / promgn
        print("")
        print("Sin notas:", ", ".join(sin_notas))
        print("Promedio General: ", f'{prom:<4.3f}')
        print("Mejor Ramo: ", maxin, "Con ", maxia)
        print("Peor Ramo: ", minin, "Con", minia)
    else:
        print("No Hay Notas Registradas.")
def guardar_notas(ramos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(ramos, archivo)
def cargar_notas(
    ):
    try:
        with open(ARCHIVO, "r") as archivo:
            ramos = json.load(archivo)
        return ramos
    except (FileNotFoundError,  json.JSONDecodeError) :
        ramos = {
            "mtm": [],
            "lng": [],
            "hst": [],
            "ing": [],
            "fsc": [],
            "qmc": [],
            "blg": []
        }
        guardar_notas(ramos)
        return ramos
def eliminar_nota(ramos):
    ingresado = False
    eliminar = ""
    while not ingresado:
        nt = 0
        if eliminar == "":
            eliminar = input("Ingrese ramo que quieras eliminar nota: ")
        if eliminar == "0":
            return
        if eliminar in ramos and len(ramos[eliminar]) != 0:
            print("Ramo: ", eliminar)
            print("")
            print("Notas:")
            for e in ramos[eliminar]:
                nt = nt + 1
                print(nt, ".  ", e)
            try:
                numero = int(input("¿Que nota quieres eliminar?"))
                if numero == 0:
                    return
                if 0 < numero <= len(ramos[eliminar]):
                    nota_eliminada = ramos[eliminar].pop(numero - 1)
                    print("")
                    print("Nota", nota_eliminada, "eliminada.")
                    ingresado = True
                    guardar_notas(ramos)
                else:
                    print("Ingresa un numero perteneciente a una nota")
            except ValueError:
                print("Ingresa un numero entero.")
        elif eliminar in ramos:
            print("El ramo no tiene notas.")
            eliminar = ""
        else:
            print("Ingrese un ramo existente.")
            eliminar = ""
def editar_nota(ramos):
    ingresado = False
    editar = ""
    while not ingresado:
        if editar == "":
           editar = input("¿Qué ramo quieres editar nota?")
        if editar in ramos and len(ramos[editar]) != 0:
            nt = 0
            print("Ramo: ", editar)
            print("")
            print("Notas:")
            for e in ramos[editar]:
                nt = nt + 1
                print(nt, ".  ", e)
            try:
                ednt = int(input("¿Qué nota quieres editar?"))
                if ednt == 0:
                    return
                if 0 < ednt <= len(ramos[editar]):
                    oldnt = ramos[editar][ednt - 1]
                    newnt = float(input("¿Cual es la nueva nota?"))
                    if newnt == 0:
                        return
                    if 1 <= newnt <= 7 and newnt != oldnt:
                        ramos[editar][ednt - 1] = newnt
                        guardar_notas(ramos)
                        print("Nota", oldnt, "Cambiada por", newnt)
                        ingresado = True
                    elif oldnt != newnt:
                        print("Ingrese una nota compatible.")
                    else:
                        print("Ingresa una nota distinta.")
                else:
                    print("Ingresa un numero perteneciente a una nota")
            except ValueError:
                print("Ingresa numeros entero.")
        elif editar == "0":
            ingresado = True
            return
        elif editar in ramos:
            print("El ramo no tiene notas.")
            editar = ""
        else:
            print("Ingrese un Ramo que exista.")
            editar = ""
def ver_evaluaciones():
    if len(eva) != 0:
        for e in eva:
            print(f'{nombres_ramos[e["ramo"]]:<11} | {e["nombre"]:<30} | {e["tipo"]:<9} | {e["fecha"]:<10} | {"Prioridad: " + str(e["prioridad"]):<12} | {e["estado"]:<9}')
    else:
        print("No Hay Evaluaciones:")
def agregar_evaluaciones():
    ramo = ""
    nombre = ""
    fecha = ""
    tipo = 20
    priori = ""
    while True:
        if ramo == "":
            ramo = input("Ramo: ")
        if ramo == "0":
            return
        if ramo in ramos:
            if nombre == "":
                nombre = input("Nombre: ")
                if nombre == "0":
                    return
                if fecha == "":
                    while fecha == "":
                        fecha =input("Nueva fecha (YYYY-MM-DD): ")
                        if fecha == "0":
                            return
                        try:
                            datetime.strptime(fecha, "%Y-%m-%d")
                        except ValueError:
                            print("Ingresa Una Fecha Valida")
                            fecha = ""
                    while True:
                        if tipo == 20:
                            print("Ingrese tipo:")
                            print("1. Prueba")
                            print("2. Lectura")
                            print("3. Trabajo")
                            print("4. Proceso")
                            try:
                                tipo = int(input("Ingrese Tipo De Evaluación: "))
                                if tipo == 0:
                                    return
                                if 0 < tipo < 5:
                                    tipo = tipsos[tipo - 1]
                                    while True:
                                        try:
                                            if priori == "":
                                                priori = int(input("Prioridad 1 al 3: "))
                                                if priori == 0:
                                                    return
                                                if 0 < priori < 4:
                                                    print("Ingrese Estado")
                                                    print("1. Pendiente")
                                                    print("2. Preparada")
                                                    print("3. Evaluada")
                                                    while True:
                                                        try:
                                                            estado = int(input("Estado 1/3: "))
                                                            if estado == 0:
                                                                return
                                                            if 0 < estado < 4:
                                                                estado = estd[estado - 1]
                                                                nueva_eva = {
                                                                    "ramo": ramo,
                                                                    "nombre": nombre,
                                                                    "fecha": fecha,
                                                                    "tipo": tipo,
                                                                    "prioridad": priori,
                                                                    "estado": estado
                                                                }
                                                                eva.append(nueva_eva)
                                                                print("Evaluacion Agregada")
                                                                guardar_evaluaciones()
                                                                return

                                                            else:
                                                                print("Ingrese un numero del 1 al 3")
                                                        except ValueError:
                                                            print("Ingresa numeros Enteros")

                                                else:
                                                    print("Ingrese número de la escala")
                                                    priori = ""
                                        except ValueError:
                                            print("Ingresa Numeros Enteros")
                                else:
                                    print("Ingrese Evaluacion Posible")
                                    tipo = 20
                            except ValueError:
                                print("Ingrese numeros")
                                tipo = 20
        else:
            print("Ingrese un Ramo existente")
            ramo = ""
def proximas_evaluaciones(lim=7):
    hoy = datetime.today().date()
    ordns = sorted(eva, key=lambda e: e["fecha"])
    if len(eva) != 0:
        for e in ordns:
            fecha_real = datetime.strptime(e["fecha"], "%Y-%m-%d").date()
            dias = (fecha_real - hoy).days
            if 0 == dias and e["estado"] != "evaluada":
                print(f'{e["nombre"]:<30} | {e["tipo"]:<9} | {"Prioridad: " + str(e["prioridad"]):<12} | {"Hoy":<4}')
            if 1 == dias and e["estado"] != "evaluada":
                print(f'{e["nombre"]:<30} | {e["tipo"]:<9} | {"Prioridad: " + str(e["prioridad"]):<12} | {"Mañana":<7}')
            if 2 <= dias <= lim and e["estado"] != "evaluada":
                print(f'{e["nombre"]:<30} | {e["tipo"]:<9} | {"Prioridad: " + str(e["prioridad"]):<12} | {"Faltan " + str(dias) + " dias":<14}')
    else:
        print("No Hay Evaluaciones.")
def editar_evaluacion():
    slct = ""
    numer = ""
    if len(eva) != 0:
        while True:
            try:
                if slct == "":
                    for i, e in enumerate(eva):
                        print(f'{str(i + 1):<3} | {nombres_ramos[e["ramo"]]:<11} | {e["nombre"]:<30} | {e["tipo"]:<9} | {e["fecha"]:<10} | {"Prioridad: " + str(e["prioridad"]):<12} | {e["estado"]:<9}')
                    slct = int(input("¿Qué Evaluación Quieres Editar?: "))
                    slct = slct - 1
                if slct == -1:
                    return
                elif -1 < slct < len(eva):
                    while True:
                        if numer == "":
                            print("Opciones A Editar")
                            print("")
                            for i, e in enumerate(campo):
                                print(i + 1, e)
                            try:
                                numer = int(input("¿Qué Deseas Editar?: "))
                            except ValueError:
                                print("Ingrese Números Enteros.")
                                numer = 13141509
                            if numer == 13141509:
                                numer = ""
                            elif numer == 0:
                                return
                            elif 1 <= numer <= len(campo):
                                zne = campo[numer - 1]
                                print("Valor Actual: ", eva[slct][zne])
                                while True:
                                    try:
                                        if zne == "fecha":
                                            while True:
                                                nw =input("Nueva fecha (YYYY-MM-DD): ")
                                                if nw == "0":
                                                    return
                                                try:
                                                    datetime.strptime(nw, "%Y-%m-%d")
                                                    eva[slct][zne] = nw
                                                    guardar_evaluaciones()
                                                    print("Fecha actualizada")
                                                    return
                                                except ValueError:
                                                    print("Ingresa Una Fecha Valida")
                                        elif zne == "nombre":
                                            nw = input("¿Qué Nombre Quieres Poner?: ")
                                            if nw == "0":
                                                return
                                            if nw == "":
                                                print("Ingresa Un Nombre")
                                            else:
                                                eva[slct][zne] = nw
                                                guardar_evaluaciones()
                                                print("Nombre Actualizado")
                                                return
                                        elif zne == "ramo":
                                            nw = input("¿Cual Es El Nuevo Ramo?")
                                            if nw == "0":
                                                return
                                            if nw in ramos:
                                                eva[slct][zne] = nw
                                                guardar_evaluaciones()
                                                print("Ramo Actualizado")
                                                return
                                            else:
                                                print("Ingrese Un Ramo Existente.")
                                        elif zne == "prioridad":
                                            nw = int(input("Ingrese Una Prioridad 1 Al 3: "))
                                            if nw == 0:
                                                return
                                            if 1 <= nw <= 3:
                                                eva[slct][zne] = nw
                                                guardar_evaluaciones()
                                                print("Prioridad Actualizada")
                                                return
                                            else:
                                                print("")
                                        elif zne == "tipo":
                                            for i in range(len(tipsos)):
                                                print(i + 1, tipsos[i])
                                            nw = int(input("Ingrese el Número Del Tipo: "))
                                            if nw == 0:
                                                return
                                            if 1 <= nw <= len(tipsos):
                                                nw = tipsos[nw - 1]
                                                eva[slct][zne] = nw
                                                guardar_evaluaciones()
                                                print("Tipo Actualizado.")
                                                return
                                            else:
                                                print("Ingrese Un Tipo Existente.")
                                        elif zne == "estado":
                                            for i in range(len(estd)):
                                                print(i +1, estd[i])
                                            nw = int(input("Ingresa el Número Del Estado: "))
                                            if nw == 0:
                                                return
                                            if 1 <= nw <= len(estd):
                                                nw = estd[nw - 1]
                                                eva[slct][zne] = nw
                                                guardar_evaluaciones()
                                                print("Estado Actualizado.")
                                                return
                                            else:
                                                print("Ingrese Un Estado Existente.")
                                                
                                    except ValueError:
                                        print("Ingresa Números Enteros")
                                        
                            else:
                                print("Ingresa Un Número De La Lista.")
                                numer = ""
                else:
                    print("Ingresa Una Evalucion Existente.")
                    slct = ""
            except ValueError:
                print("Ingresa Numeros Enteros")
                slct = ""
    else:
        print("No Hay Evaluaciones")
def eliminar_evaluacion():
    elmn = ""
    if len(eva) != 0:
        for i, e in enumerate(eva):
            print(f'{str(i + 1):<3} | {nombres_ramos[e["ramo"]]:<11} | {e["nombre"]:<30} | {e["tipo"]:<9} | {e["fecha"]:<10} | {"Prioridad: " + str(e["prioridad"]):<12} | {e["estado"]:<9}')
        while True:
            try:
                if elmn == "":
                    elmn = int(input("¿Qué Evaluación Quieres Eliminar?: "))
                if elmn == 0:
                    return
                if 1 <= elmn <= len(eva):
                    elmn = elmn -1
                    while True:
                        try:
                            print("¿Seguro De Que Quieres Eliminar", eva[elmn]["tipo"], nombres_ramos[eva[elmn]["ramo"]], "?")
                            print("1. Sí")
                            print("2. No")
                            rsp = int(input("Ingrese Número De Opción: "))
                            if rsp == 1:
                                eva.pop(elmn)
                                print("Evaluación Eliminada")
                                guardar_evaluaciones()
                                return
                            elif rsp == 2:
                                return
                            elif rsp == 0:
                                return
                            else:
                                print("Ingresa 1,2 o 0 para salir")
                                print("")
                        except ValueError:
                            print("Ingresa Números Enteros.")
                else:
                    print("Ingrese Un Número De La Lista.")
                    elmn = ""
            except ValueError:
                print("Ingrese Números")
    else:
        print("No Hay Evaluciones.")
def guardar_evaluaciones():
    with open(ARCHIVO_EVA, "w") as archivo:
        json.dump(eva, archivo, indent=4)
def cargar_evaluaciones():
    try:
        with open(ARCHIVO_EVA, "r") as archivo:
            return json.load(archivo)

    except (FileNotFoundError, json.JSONDecodeError):
        return []
def obtener_promedios(ramos):
    proms = {}
    for r, n in ramos.items():
        if len(n) > 0:
            prom = sum(n) / len(n)
            proms[r] = prom
    return proms
def graficar_promedios(ramos):
    proms = obtener_promedios(ramos)
    rmo = list(proms.keys())
    val = list(proms.values())
    bs = plt.bar(rmo, val)
    plt.bar(rmo, val)
    plt.ylim(1, 7.5)
    plt.title("Promedios Por Ramo")
    plt.xlabel("Ramo")
    plt.ylabel("Promedio")
    for b, v in zip(bs, val):
        plt.text(
            b.get_x() + b.get_width() / 2,
            b.get_height()+ 0.05,
            f"{v:.2f}",
            ha="center",
            va="bottom"
        )
    plt.show()
def graficar_evolucion(ramos):
    c = ""
    while c == "":
        c = input("¿Qué Ramo Quieres Ver Evolución?")
        if c == "0":
            return
        if  c in ramos:
            if len(ramos[c]) == 0:
                print("No Hay Notas")
                c = ""
        else:
            print("Ingrese Un Ramo Existente.")
            c = ""
    nt = ramos[c]
    evols = list(range(1, len(nt) + 1))
    prm = sum(nt) / len(nt)
    plt.plot(evols, nt, marker="o", label="Notas")
    if len(nt) >= 2:
        m, b = calcular_tendencia(nt)
        tendencia = [m * xi + b for xi in evols]
        plt.plot(evols, tendencia, label="Tendencia")
    plt.axhline(
        y=prm,
        linestyle="--",
        label=f"Promedio: {prm: .2f}"
        )
    plt.ylim(1, 7.5)
    plt.title(f"Evolución de notas - {c}")
    plt.xlabel("Evaluación")
    plt.ylabel("Nota")
    plt.legend()
    plt.show()
def calcular_tendencia(n):
    if len(n) < 2:
        return None
    x = list(range(1, len(n) + 1))
    prmx = sum(x) / len(x)
    prmy = sum(n) / len(n)
    nmr = 0
    dno = 0
    for xi, yi in zip(x, n):
        nmr += (xi - prmx)*(yi - prmy)
        dno += (xi - prmx)**2
    pnd = nmr / dno
    b = prmy - prmx * pnd
    return (pnd, b)
def calcular_varianza(n):
    if len(ramos[n]) < 2:
        return 0
    prm = sum(ramos[n]) / len(ramos[n])
    p = 0
    vr = 0
    for e in ramos[n]:
        p = (e - prm) ** 2
        vr += p
    vr = vr / len(ramos[n])
    return vr
def calcular_desviacion(n):
    o = calcular_varianza(n)
    if o == 0:
        return 0
    o = o ** 0.5
    return o
def interpretar_tendencia(n):
    if len(ramos[n]) < 2:
        return "Notas Insuficientes."
    m, b = calcular_tendencia(ramos[n])
    if m > 0:
        return "Ascendente."
    elif m < 0:
        return "Descendente."
    return "Sin Tendencia Lineal."
ramos = cargar_notas()
eva = cargar_evaluaciones()
ingresado = False
opcion = ""
opcion_2 = ""
opcion_1 = ""
opcion_3 = ""
while opcion != "0":
    print("\n ===StudyTracker.V3===")
    print("1. Notas")
    print("2. Evaluaciones")
    print("3. Resumen Académico")
    print("0. Salir")
    opcion = input("Ingrese Opción: ")
    opcion_2 = ""
    opcion_1 = ""
    opcion_3 = ""
    if opcion == "1":
        while opcion_1 != "0":
            print("")
            print(" ===NOTAS=== ")
            print("")
            print("1. Agregar Nota")
            print("2. Ver Notas")
            print("3. Editar Nota")
            print("4. Eliminar Nota")
            print("0. volver")
            opcion_1 = input("Ingrese Opción: ")
            if opcion_1 == "1":
                agregar_notas(ramos)
            elif opcion_1 == "2":
                ver_notas(ramos)
            elif opcion_1 == "3":
                editar_nota(ramos)
            elif opcion_1 == "4":
                eliminar_nota(ramos)
     
    elif opcion == "2":
        while opcion_2 != "0":
            print("")
            print(" ===EVALUACIONES=== ")
            print("")
            print("1. Agregar Evaluación")
            print("2. Ver Evaluaciones")
            print("3. Próximas Evaluaciones")
            print("4. Editar Evaluación")
            print("5. Eliminar Evaluación")
            print("0. volver")
            opcion_2 = input("Ingrese Opción: ")
            if opcion_2 == "1":
                agregar_evaluaciones()
            elif opcion_2 == "2":
                ver_evaluaciones()
            elif opcion_2 == "3":
                proximas_evaluaciones(14)
            elif opcion_2 == "4":
                editar_evaluacion()
            elif opcion_2 == "5":
                eliminar_evaluacion()
    elif opcion == "3":
        while opcion_3 != "0":
            print("")
            print(" ===RESUMEN ACADÉMICO=== ")
            print("")
            print("1. Ver Notas")
            print("2. Promédio General")
            print("3. Próximas Evaluaciones")
            print("4. Graficar Evolución")
            print("0. volver")
            opcion_3 = input("Ingrese Opción: ")
            if opcion_3 == "1":
                ver_notas(ramos)
            elif opcion_3 == "2":
                ver_resumen_general(ramos)
            elif opcion_3 == "3":
                proximas_evaluaciones(14)
            elif opcion_3 == "4":
                graficar_evolucion(ramos)
