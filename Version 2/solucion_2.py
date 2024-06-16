class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

class NodoJugador:
    def __init__(self, jugador):
        self.jugador = jugador
        self.siguiente = None

class ListaEnlazadaJugadores:
    def __init__(self):
        self.cabeza = None

    def agregar(self, jugador):
        nuevo_nodo = NodoJugador(jugador)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def to_list(self):
        jugadores = []
        actual = self.cabeza
        while actual:
            jugadores.append(actual.jugador)
            actual = actual.siguiente
        return jugadores

    def bubble_sort(self):
        jugadores = self.to_list()
        n = len(jugadores)
        for i in range(n):
            for j in range(0, n-i-1):
                if (jugadores[j].rendimiento > jugadores[j+1].rendimiento or
                    (jugadores[j].rendimiento == jugadores[j+1].rendimiento and jugadores[j+1].edad < jugadores[j].edad)):
                    jugadores[j], jugadores[j+1] = jugadores[j+1], jugadores[j]
        self.cabeza = None
        for jugador in reversed(jugadores):
            self.agregar(jugador)

class EquipoConRendimiento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = ListaEnlazadaJugadores()

    def agregar_jugador(self, jugador):
        self.jugadores.agregar(jugador)

    def rendimiento_promedio(self):
        jugadores = self.jugadores.to_list()
        return sum(jugador.rendimiento for jugador in jugadores) / len(jugadores) if jugadores else 0

    def __str__(self):
        return f"{self.nombre} (Rendimiento Promedio: {self.rendimiento_promedio()})"

class SedeConRendimiento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def rendimiento_total(self):
        return sum(equipo.rendimiento_promedio() for equipo in self.equipos)

    def __str__(self):
        return f"{self.nombre} (Rendimiento Total: {self.rendimiento_total()})"

def bubble_sort_equipos(equipos):
    n = len(equipos)
    for i in range(n):
        for j in range(0, n-i-1):
            if (equipos[j].rendimiento_promedio() > equipos[j+1].rendimiento_promedio() or
                (equipos[j].rendimiento_promedio() == equipos[j+1].rendimiento_promedio() and len(equipos[j].jugadores.to_list()) < len(equipos[j+1].jugadores.to_list()))):
                equipos[j], equipos[j+1] = equipos[j+1], equipos[j]

def rendimiento_promedio_sede(sede):
    return (sede.rendimiento_total(), -len(sede.equipos))

def rendimiento_promedio_jugador(jugador):
    return (jugador.rendimiento, jugador.edad)

def ordenar_y_mostrar_datos(sedes):
    todos_jugadores = []
    for sede in sedes:
        for equipo in sede.equipos:
            equipo.jugadores.bubble_sort()
            todos_jugadores.extend(equipo.jugadores.to_list())
        bubble_sort_equipos(sede.equipos)
    sedes.sort(key=rendimiento_promedio_sede)

    print("Datos de Sedes y Equipos:")
    for sede in sedes:
        rendimiento_sede = sede.rendimiento_total()
        print(f"Sede {sede.nombre}, Rendimiento: {rendimiento_sede}")
        for equipo in sede.equipos:
            promedio_rendimiento = equipo.rendimiento_promedio()
            jugadores_ordenados = ', '.join(f"{jugador.id}" for jugador in equipo.jugadores.to_list())
            print(f"{equipo.nombre}, Rendimiento: {promedio_rendimiento}")
            print(f"{{{jugadores_ordenados}}}")

    todos_jugadores.sort(key=rendimiento_promedio_jugador)
    print("\nRanking de Jugadores:")
    print("[" + ", ".join(str(jugador.id) for jugador in todos_jugadores) + "]")

    jugador_max_rendimiento = max(todos_jugadores, key=rendimiento_promedio_jugador)
    jugador_min_rendimiento = min(todos_jugadores, key=rendimiento_promedio_jugador)
    jugador_mas_joven = min(todos_jugadores, key=lambda j: j.edad)
    jugador_mas_veterano = max(todos_jugadores, key=lambda j: j.edad)
    promedio_edad = sum(jugador.edad for jugador in todos_jugadores) / len(todos_jugadores)
    promedio_rendimiento = sum(jugador.rendimiento for jugador in todos_jugadores) / len(todos_jugadores)
    
    def rendimiento_promedio_equipo(equipo_sede_tuple):
        return equipo_sede_tuple[0].rendimiento_promedio()

    equipo_max_rendimiento = max([(equipo, sede) for sede in sedes for equipo in sede.equipos], key=rendimiento_promedio_equipo)
    equipo_min_rendimiento = min([(equipo, sede) for sede in sedes for equipo in sede.equipos], key=rendimiento_promedio_equipo)
    
    print("\nEstadísticas:")
    print(f"Equipo con mayor rendimiento: {equipo_max_rendimiento[0].nombre} en sede {equipo_max_rendimiento[1].nombre}")
    print(f"Equipo con menor rendimiento: {equipo_min_rendimiento[0].nombre} en sede {equipo_min_rendimiento[1].nombre}")
    print(f"Jugador con mayor rendimiento: {jugador_max_rendimiento.id}, {jugador_max_rendimiento.nombre}, {jugador_max_rendimiento.rendimiento}")
    print(f"Jugador con menor rendimiento: {jugador_min_rendimiento.id}, {jugador_min_rendimiento.nombre}, {jugador_min_rendimiento.rendimiento}")
    print(f"Jugador más joven: {jugador_mas_joven.id}, {jugador_mas_joven.nombre}, {jugador_mas_joven.edad}")
    print(f"Jugador más veterano: {jugador_mas_veterano.id}, {jugador_mas_veterano.nombre}, {jugador_mas_veterano.edad}")
    print(f"Promedio de edad de los jugadores: {promedio_edad}")
    print(f"Promedio del rendimiento de los jugadores: {promedio_rendimiento}")