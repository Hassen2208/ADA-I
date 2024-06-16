import time
import pruebas
from solucion_1 import ordenar_y_mostrar_datos as ordenar_y_mostrar_datos_1, SedeConRendimiento as SedeConRendimiento_1, EquipoConRendimiento as EquipoConRendimiento_1
from solucion_2 import ordenar_y_mostrar_datos as ordenar_y_mostrar_datos_2, SedeConRendimiento as SedeConRendimiento_2, EquipoConRendimiento as EquipoConRendimiento_2, ListaEnlazadaJugadores

if __name__ == "__main__":
    try:
        num_jugadores = int(input("Ingrese la cantidad de jugadores que desea organizar: "))
        num_sedes = int(input("Ingrese la cantidad de sedes que desea generar: "))
        num_deportes = int(input("Ingrese la cantidad de deportes que desea generar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        exit(1)

    # Validar las restricciones
    if num_sedes < 2:
        print("Debe haber al menos 2 sedes.")
        exit(1)

    if num_deportes < 2:
        print("Debe haber al menos 2 deportes.")
        exit(1)

    # Generar datos de prueba
    jugadores = pruebas.generar_jugadores(num_jugadores)
    sedes = pruebas.generar_sedes_y_equipos(jugadores, num_sedes, num_deportes)

    # Mostrar jugadores generados
    pruebas.mostrar_jugadores(jugadores)

    # Aplicar solución 1 y medir el tiempo
    print("\nSolución 1:")
    sedes_1 = [SedeConRendimiento_1(sede.ciudad) for sede in sedes]
    for sede, sede_1 in zip(sedes, sedes_1):
        for equipo in sede.equipos:
            equipo_1 = EquipoConRendimiento_1(equipo.deporte)
            equipo_1.jugadores = equipo.jugadores.copy()
            sede_1.agregar_equipo(equipo_1)
    
    start_time = time.time()
    ordenar_y_mostrar_datos_1(sedes_1)
    end_time = time.time()
    print(f"Tiempo de ejecución Solución 1: {end_time - start_time} segundos")

    # Aplicar solución 2 y medir el tiempo
    print("\nSolución 2:")
    sedes_2 = [SedeConRendimiento_2(sede.ciudad) for sede in sedes]
    for sede, sede_2 in zip(sedes, sedes_2):
        for equipo in sede.equipos:
            equipo_2 = EquipoConRendimiento_2(equipo.deporte)
            lista_jugadores = ListaEnlazadaJugadores()
            for jugador in equipo.jugadores:
                lista_jugadores.agregar(jugador)
            equipo_2.jugadores = lista_jugadores
            sede_2.agregar_equipo(equipo_2)
    
    start_time = time.time()
    ordenar_y_mostrar_datos_2(sedes_2)
    end_time = time.time()
    print(f"Tiempo de ejecución Solución 2: {end_time - start_time} segundos")
