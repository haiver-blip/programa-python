# ============================================================
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación - Código: 213022
# Fase 5 - Evaluación Final POA
# Problema 1: Nivel de compromiso de sesiones de clientes
# Estudiante: Haiver Riaño Riaño
# ============================================================

# Datos iniciales: matriz con información de sesiones de clientes
# Formato: [ID Cliente, Duración (segundos), Eventos Clics]
sesiones = [
    ["C001", 210, 12],
    ["C002", 45,  2],
    ["C003", 130, 6],
    ["C004", 300, 10],
    ["C005", 55,  9],
    ["C006", 190, 3],
    ["C007", 80,  1],
]


# Función que clasifica el nivel de compromiso de una sesión
# según su duración en segundos y el número de clics registrados
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# Función que recorre la matriz y genera el informe de compromiso
def generar_informe(matriz):
    print("=" * 45)
    print("   INFORME DE NIVEL DE COMPROMISO POR SESIÓN")
    print("=" * 45)
    print(f"{'ID Cliente':<12} {'Duración (s)':<15} {'Clics':<8} {'Nivel'}")
    print("-" * 45)

    for fila in matriz:
        id_cliente = fila[0]
        duracion   = fila[1]
        clics      = fila[2]

        nivel = clasificar_compromiso(duracion, clics)

        print(f"{id_cliente:<12} {duracion:<15} {clics:<8} {nivel}")

    print("=" * 45)


# Punto de entrada principal del programa
def main():
    print("\nIniciando análisis de sesiones de clientes...\n")
    generar_informe(sesiones)
    print("\nAnálisis finalizado.")


main()
