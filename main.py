# pedir el nombre de dos equipos al usuario
def pedir_equipo(equipo):
    nombre = input(f"Ingrese el nombre del equipo {equipo}: ")
    return nombre

# pedir los puntos de los equipos al usuario
def pedir_puntos(equipo):
    puntos = int(input(f"Ingrese los puntos del equipo {equipo}: "))
    return puntos

# determinar el ganador del set
def jugar_set(equipo_a, equipo_b):
    puntos_a = pedir_puntos(equipo_a)
    puntos_b = pedir_puntos(equipo_b)

    diferencia = abs(puntos_a - puntos_b)

# Caso 1: alguien llega a 25 puntos exactos con al menos 2 de diferencia
    if (puntos_a == 25 or puntos_b == 25) and diferencia >= 2:
        if puntos_a > puntos_b:
            print(f"Gana el set {equipo_a}")
            return equipo_a
        else:
            print(f"Gana el set {equipo_b}")
            return equipo_b

# Caso 2: se supera el 25 (debe haber EXACTAMENTE 2 de diferencia)
    if puntos_a > 25 or puntos_b > 25:
        if diferencia == 2:
            if puntos_a > puntos_b:
                print(f"Gana el set {equipo_a}")
                return equipo_a
            else:
                print(f"Gana el set {equipo_b}")
                return equipo_b

    print("El set no es válido. Debe ganarse con 25 puntos o más y 2 de diferencia.")
    return None
    
def main():

# imprimir mensaje de bienvenida
    print("=======================================================")
    print("Bienvenido al programa de gestión de partidos de Voley.")
    print("=======================================================")

# pedir nombres de los equipos
    equipo_a = pedir_equipo("A")
    equipo_b = pedir_equipo("B")

# mostrar los equipos registrados
    print("-----------------------------------------------------------------")
    print(f"Los equipos registrados son: Local: {equipo_a} y Visitante: {equipo_b}.")
    print("-----------------------------------------------------------------")

# cargar los puntos de cada set
    num_set = 1
    sets_a = 0
    sets_b = 0

# jugar los sets hasta que un equipo gane 3 sets
    while num_set <= 5 and sets_a < 3 and sets_b < 3:
        print(f"\n--- Set {num_set} ---")
        ganador = jugar_set(equipo_a, equipo_b)

        if ganador == equipo_a:
            sets_a += 1
            num_set += 1
        elif ganador == equipo_b:
            sets_b += 1
            num_set += 1
        else:
            print("Repetimos el set.")

    print("-----------------------------------------------------------------")
    print(f"Resultado final: {equipo_a} {sets_a} - {sets_b} {equipo_b}")
    print("-----------------------------------------------------------------")

if __name__ == "__main__":
    main()  
    