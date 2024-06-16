class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

class EquipoConRendimiento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def rendimiento_promedio(self):
        return sum(jugador.rendimiento for jugador in self.jugadores) / len(self.jugadores) if self.jugadores else 0

    def __str__(self):
        return f"{self.nombre} (Rendimiento Promedio: {self.rendimiento_promedio()})"

class SedeConRendimiento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def rendimiento_promedio(self):
        return sum(equipo.rendimiento_promedio() for equipo in self.equipos) / len(self.equipos) if self.equipos else 0

    def __str__(self):
        return f"{self.nombre} (Rendimiento Promedio: {self.rendimiento_promedio()})"

def insertion_sort_jugadores(jugadores):
    for i in range(1, len(jugadores)):
        key = jugadores[i]
        j = i - 1
        while j >= 0 and (jugadores[j].rendimiento > key.rendimiento or 
                          (jugadores[j].rendimiento == key.rendimiento and jugadores[j].edad < key.edad)):
            jugadores[j + 1] = jugadores[j]
            j -= 1
        jugadores[j + 1] = key

def selection_sort_equipos(equipos):
    for i in range(len(equipos)):
        min_idx = i
        for j in range(i + 1, len(equipos)):
            if (equipos[j].rendimiento_promedio() < equipos[min_idx].rendimiento_promedio() or
                (equipos[j].rendimiento_promedio() == equipos[min_idx].rendimiento_promedio() and len(equipos[j].jugadores) > len(equipos[min_idx].jugadores))):
                min_idx = j
        equipos[i], equipos[min_idx] = equipos[min_idx], equipos[i]

def rendimiento_promedio_sede(sede):
    return (sede.rendimiento_promedio(), -len(sede.equipos))

def rendimiento_promedio_jugador(jugador):
    return (jugador.rendimiento, jugador.edad)

def ordenar_y_mostrar_datos(sedes):
    todos_jugadores = []
    for sede in sedes:
        for equipo in sede.equipos:
            insertion_sort_jugadores(equipo.jugadores)
            todos_jugadores.extend(equipo.jugadores)
        selection_sort_equipos(sede.equipos)
    sedes.sort(key=rendimiento_promedio_sede)

    print("Datos de Sedes y Equipos:")
    for sede in sedes:
        print(f"Sede {sede.nombre}:")
        for equipo in sede.equipos:
            promedio_rendimiento = equipo.rendimiento_promedio()
            jugadores_ordenados = ', '.join(f"{jugador.id}" for jugador in equipo.jugadores)
            print(f"{equipo.nombre}, Rendimiento: {promedio_rendimiento}")
            print(f"{{{jugadores_ordenados}}}")

    insertion_sort_jugadores(todos_jugadores)
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

