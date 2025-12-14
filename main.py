# pedir el nombre de dos equipos al usuario
def pedir_equipo(equipo):
    nombre = input(f"Ingrese el nombre del equipo {equipo}: ")
    return nombre

# pedir los puntos de los equipos al usuario
def pedir_puntos(equipo):
    puntos = int(input(f"Ingrese los puntos del equipo {equipo}: "))
    return puntos

def jugar_set(equipo_a, equipo_b):
    puntos_a = pedir_puntos(equipo_a)
    puntos_b = pedir_puntos(equipo_b)

    if puntos_a > puntos_b:
        print(f"Gana el set {equipo_a}")
        return "A"
    elif puntos_b > puntos_a:
        print(f"Gana el set {equipo_b}")
        return "B"
    else:
        print("Error: Los puntos no pueden ser iguales en un set de Vóley.")
        return None
    
# imprimir mensaje de bienvenida
print("=======================================================")
print("Bienvenido al programa de gestión de partidos de Voley.")
print("=======================================================")

# pedir nombres de los equipos
def main():
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

    while num_set <= 5 and sets_a < 3 and sets_b < 3:
        print(f"\n--- Set {num_set} ---")

        ganador = jugar_set(equipo_a, equipo_b)

        if ganador == "A":
            sets_a += 1
            num_set += 1
        elif ganador == "B":
            sets_b += 1
            num_set += 1
        else:
            print("Repetimos el set.")

    print("-----------------------------------------------------------------")
    print(f"Resultado final: {equipo_a} {sets_a} - {sets_b} {equipo_b}")
    print("-----------------------------------------------------------------")

if __name__ == "__main__":
    main()  
    