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

    def rendimiento_total(self):
        return sum(equipo.rendimiento_promedio() for equipo in self.equipos)

    def __str__(self):
        return f"{self.nombre} (Rendimiento Total: {self.rendimiento_total()})"

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
    return (sede.rendimiento_total(), -len(sede.equipos))

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
        rendimiento_sede = sede.rendimiento_total()
        print(f"Sede {sede.nombre}, Rendimiento: {rendimiento_sede}")
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
# Ejemplo de uso
jugadores = {
    1: Jugador(1, "Sofia Garcia", 21, 66),
    2: Jugador(2, "Alejandro Torres", 27, 24),
    3: Jugador(3, "Valentina Rodriguez", 19, 15),
    4: Jugador(4, "Juan Lopez", 22, 78),
    5: Jugador(5, "Martina Martinez", 30, 55),
    6: Jugador(6, "Sebastian Perez", 25, 42),
    7: Jugador(7, "Camila Fernandez", 24, 36),
    8: Jugador(8, "Mateo Gonzalez", 29, 89),
    9: Jugador(9, "Isabella Diaz", 40, 92),
    10: Jugador(10, "Daniel Ruiz", 17, 57),
    11: Jugador(11, "Luciana Sanchez", 18, 89),
    12: Jugador(12, "Lucas Vasquez", 26, 82),
    13: Jugador(13, "William Hernandez", 30, 44),
    14: Jugador(14, "Laura Perez", 20, 78),
    15: Jugador(15, "Santiago Rodriguez", 23, 32),
    16: Jugador(16, "Maria Gonzalez", 28, 65),
    17: Jugador(17, "Carlos Lopez", 19, 72),
    18: Jugador(18, "Valeria Martinez", 21, 45),
    19: Jugador(19, "Andres Perez", 30, 78),
    20: Jugador(20, "Sara Hernandez", 22, 56)
}

sede_cali = SedeConRendimiento("Cali")
equipo_futbol_cali = EquipoConRendimiento("Futbol")
equipo_futbol_cali.agregar_jugador(jugadores[10])
equipo_futbol_cali.agregar_jugador(jugadores[2])
sede_cali.agregar_equipo(equipo_futbol_cali)

equipo_volleyball_cali = EquipoConRendimiento("Volleyball")
equipo_volleyball_cali.agregar_jugador(jugadores[1])
equipo_volleyball_cali.agregar_jugador(jugadores[9])
equipo_volleyball_cali.agregar_jugador(jugadores[12])
equipo_volleyball_cali.agregar_jugador(jugadores[6])
sede_cali.agregar_equipo(equipo_volleyball_cali)

equipo_basketball_cali = EquipoConRendimiento("Basketball")
equipo_basketball_cali.agregar_jugador(jugadores[13])
equipo_basketball_cali.agregar_jugador(jugadores[14])
equipo_basketball_cali.agregar_jugador(jugadores[15])
equipo_basketball_cali.agregar_jugador(jugadores[16])
sede_cali.agregar_equipo(equipo_basketball_cali)

sede_medellin = SedeConRendimiento("Medellin")
equipo_futbol_medellin = EquipoConRendimiento("Futbol")
equipo_futbol_medellin.agregar_jugador(jugadores[11])
equipo_futbol_medellin.agregar_jugador(jugadores[8])
equipo_futbol_medellin.agregar_jugador(jugadores[7])
sede_medellin.agregar_equipo(equipo_futbol_medellin)

equipo_volleyball_medellin = EquipoConRendimiento("Volleyball")
equipo_volleyball_medellin.agregar_jugador(jugadores[3])
equipo_volleyball_medellin.agregar_jugador(jugadores[4])
equipo_volleyball_medellin.agregar_jugador(jugadores[5])
sede_medellin.agregar_equipo(equipo_volleyball_medellin)

equipo_basketball_medellin= EquipoConRendimiento("Basketball")
equipo_basketball_medellin.agregar_jugador(jugadores[17])
equipo_basketball_medellin.agregar_jugador(jugadores[18])
equipo_basketball_medellin.agregar_jugador(jugadores[19])
equipo_basketball_medellin.agregar_jugador(jugadores[20])
sede_medellin.agregar_equipo(equipo_basketball_medellin) 

sedes = [sede_cali, sede_medellin]
ordenar_y_mostrar_datos(sedes)
                                        
