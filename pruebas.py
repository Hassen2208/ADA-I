import random

class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f'Jugador({self.id}, {self.nombre}, {self.edad}, {self.rendimiento})'

class Equipo:
    def __init__(self, deporte):
        self.deporte = deporte
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Sede:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

def generar_jugadores(num_jugadores):
    nombres = ["Sofia", "Alejandro", "Valentina", "Juan", 
               "Martina", "Sebastián", "Camila", "Mateo", 
               "Isabella", "Daniel", "Luciana", "Lucas",
               "Emilia", "Diego", "Victoria"]
    
    apellidos = ["García", "Torres", "Rodriguez", "López", 
                 "Martinez", "Pérez", "Fernández", "González", 
                 "Díaz", "Ruiz", "Sánchez", "Vásquez",
                 "Ramirez", "Flores", "Ortiz"]

    jugadores = {}
    for i in range(1, num_jugadores + 1):
        nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
        edad = random.randint(10, 50)
        rendimiento = random.randint(1, 100)
        jugadores[i] = Jugador(i, nombre_completo, edad, rendimiento)
    return jugadores

def generar_sedes_y_equipos(jugadores, num_sedes, num_deportes):
    ciudades = ["Cali", "Medellín", "Bogotá", "Barranquilla", "Cartagena"]
    deportes_base = ["Futbol", "Volleyball", "Baloncesto", "Tenis"]
    deportes_base = deportes_base[:num_deportes]
    sedes = []
    jugadores_usados = set()

    for _ in range(num_sedes):
        if not ciudades:
            break
        ciudad = ciudades.pop(random.randint(0, len(ciudades) - 1))
        sede = Sede(ciudad)
        deportes = deportes_base.copy()  # Hacer una copia de la lista de deportes para cada sede
        deportes_usados = []

        # Crear al menos dos equipos
        while len(deportes_usados) < 2 and len(jugadores_usados) < len(jugadores):
            if not deportes:
                break
            deporte = deportes.pop(random.randint(0, len(deportes) - 1))
            equipo = Equipo(deporte)
            deportes_usados.append(deporte)
            
            while len(equipo.jugadores) < 2 and len(jugadores_usados) < len(jugadores):
                jugador = random.choice(list(jugadores.values()))
                if jugador.id not in jugadores_usados:
                    equipo.agregar_jugador(jugador)
                    jugadores_usados.add(jugador.id)
            
            if len(equipo.jugadores) >= 2:
                sede.agregar_equipo(equipo)

        # Crear equipos adicionales hasta que se hayan usado todos los deportes
        while len(deportes_usados) < len(deportes_base) and len(jugadores_usados) < len(jugadores):
            if not deportes:
                break
            deporte = deportes.pop(random.randint(0, len(deportes) - 1))
            equipo = Equipo(deporte)
            deportes_usados.append(deporte)
            
            while len(equipo.jugadores) < 2 and len(jugadores_usados) < len(jugadores):
                jugador = random.choice(list(jugadores.values()))
                if jugador.id not in jugadores_usados:
                    equipo.agregar_jugador(jugador)
                    jugadores_usados.add(jugador.id)

            if len(equipo.jugadores) >= 2:
                sede.agregar_equipo(equipo)
        
        if len(sede.equipos) >= 2:
            sedes.append(sede)

    # Distribuir los jugadores restantes
    for jugador in jugadores.values():
        if jugador.id not in jugadores_usados:
            sede = random.choice(sedes)
            equipo = random.choice(sede.equipos)
            equipo.agregar_jugador(jugador)
            jugadores_usados.add(jugador.id)

    return sedes

def mostrar_sedes(sedes):
    for sede in sedes:
        print(f"Sede: {sede.ciudad}")
        for equipo in sede.equipos:
            print(f"  Deporte: {equipo.deporte}")
            for jugador in equipo.jugadores:
                print(f"    {jugador}")

def mostrar_jugadores(jugadores):
    print("Lista de Jugadores Generados:")
    for jugador in jugadores.values():
        print(jugador)

if __name__ == "__main__":
    num_jugadores = int(input("Ingrese la cantidad de jugadores que desea generar: "))
    num_sedes = int(input("Ingrese la cantidad de sedes que desea generar: "))
    num_deportes = int(input("Ingrese la cantidad de deportes que desea generar: "))

    if num_sedes < 2:
        print("Debe haber al menos 2 sedes.")
        exit(1)

    if num_deportes < 2:
        print("Debe haber al menos 2 deportes.")
        exit(1)

    jugadores = generar_jugadores(num_jugadores)
    sedes = generar_sedes_y_equipos(jugadores, num_sedes, num_deportes)
    mostrar_sedes(sedes)
    mostrar_jugadores(jugadores)
