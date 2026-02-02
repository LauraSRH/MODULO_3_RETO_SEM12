#RETO SEMANA 12. Ingreso de datos y gráficas con Matplotlib

import matplotlib.pyplot as plt

def obtener_ventas_por_rango():
    """Esta función pide al usuario un rango de años y las ventas correspondientes para cada año."""
    # Paso 1: Pedir años inicial y final
    año_inicial = int(input("Año inicial (ej: 2015): "))
    año_final = int(input("Año final (ej: 2022): "))
    
    # Crear listas vacías
    años = []
    ventas = []
    
    # Paso 2: Pedir ventas para CADA año en el rango
    print(f"\n--- Ingresa las ventas para cada año ---")
    for año in range(año_inicial, año_final + 1):
        venta = float(input(f"Ventas {año}: $"))
        años.append(año)
        ventas.append(venta)
    
    return años, ventas

def graficar_ventas(años, ventas):
    """Aquí se crea y muestra la gráfica de ventas por años."""
    # Crear gráfica de líneas
    plt.figure(figsize=(6, 4))
    plt.plot(años, ventas, marker='o', linewidth=3, markersize=8, color='#2E86C1')
    
    # Personalizar gráfica
    plt.title(f'Ventas del periodo del año {años[0]} a {años[-1]}', fontsize=16, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Ventas (MXN)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Mostrar valores en puntos
    for i, venta in enumerate(ventas):
        plt.annotate(f'${venta:,.0f}', (años[i], venta), 
                    textcoords="offset points", xytext=(0,10), 
                    ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# PROGRAMA PRINCIPAL
def main():
    print("=== GRÁFICA DE VENTAS POR AÑOS ===")
    años, ventas = obtener_ventas_por_rango()
    
    print(f"\nDatos ingresados:")
    for i in range(len(años)):
        print(f"{años[i]}: ${ventas[i]:,.0f}")
    
    graficar_ventas(años, ventas)
    print("¡Gráfica generada exitosamente!")

# Ejecutar
if __name__ == "__main__":
    main()
    input("\nPresiona Enter para cerrar...")