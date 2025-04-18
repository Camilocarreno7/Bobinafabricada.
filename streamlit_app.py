import streamlit as st

def calcular_parametros(longitud_cm, diametro_cm=None):
    if diametro_cm is None:
        diametro_cm = float(input("No se ingresó diámetro. Ingrese un valor aproximado [cm]: "))
    if diametro_cm == 0:
        raise ValueError("El diámetro no puede ser cero.")

    relacion_LD = longitud_cm / diametro_cm

    if relacion_LD > 2.9:
        espiras = 5
        amperaje = 45000 / (relacion_LD * 5)
    else:
        espiras = 6
        amperaje = 45000 / (relacion_LD * 6)

    return relacion_LD, espiras, round(amperaje, 2)

# Programa principal
if __name__ == "__main__":
    print("==============================================")
    print("🔧 Bienvenido al Calculador de Espiras y Amperaje")
    print("Este programa determina el número de espiras y el amperaje-espira")
    print("recomendado según la relación Longitud / Diámetro de una pieza.")
    print("==============================================\n")

    while True:
        try:
            L = float(input("Ingrese la longitud de la pieza [cm]: "))
            D_input = input("Ingrese el diámetro de la pieza [cm] (presione Enter si no lo tiene): ")

            D = float(D_input) if D_input.strip() != "" else None

            relacion, espiras, corriente = calcular_parametros(L, D)

            print("\n📊 Resultados del cálculo:")
            print(f"Relación L/D: {round(relacion, 2)}")
            print(f"Número de espiras recomendado: {espiras}")
            print(f"Amperaje-espira a utilizar: {corriente} A\n")

        except ValueError as e:
            print(f"⚠️ Error: {e}\n")

        # Preguntar si desea realizar otro cálculo
        while True:
            repetir = input("¿Desea realizar otro cálculo? (s/n): ").strip().lower()
            if repetir in ["s", "si", "sí"]:
                print("\n🔄 Iniciando nuevo cálculo...\n")
                break
            elif repetir in ["n", "no"]:
                print("\nGracias por usar el calculador. ¡Hasta la próxima! 👋")
                exit()
            else:
                print("❗ Respuesta no válida. Por favor escriba 's' o 'n'.")

