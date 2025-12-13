# pedir el nombre de dos equipos al usuario
def pedir_equipo(equipo):
    nombre = input(f"Ingrese el nombre del equipo {equipo}: ")
    return nombre

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

if __name__ == "__main__":
    main()  
    