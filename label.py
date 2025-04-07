import os

def generar_etiquetas(archivo_entrada, archivo_salida):
    url_base = "https://script.google.com/macros/s/AKfycbzuV7k_VXlHt3922DziqnFPV-ZzxZtur0Coij7EOAZwkT11t_ukiFt_DHdyU25qCrSh/exec?ID=usuario&equipoID="
    
    with open(archivo_entrada, "r") as f:
        valores = [line.strip() for line in f if line.strip()]
    
    with open(archivo_salida, "w") as f:
        for valor in valores:
            etiqueta = f"""
^XA
^PON
^FO120,20^BQN,2,3.5^FDLA,{url_base}{valor}^FS
^FO310,45^A0N,24,24^FDINVENTARIO^FS
^FO310,80^A0N,24,24^FDEQUIPO^FS
^FO310,115^A0N,24,24^FDMEDICO   2025^FS
^FO310,180^A0N,24,24^FD{valor}^FS
^XZ

"""
            f.write(etiqueta + "\n")
    
    print(f"Etiquetas generadas en {archivo_salida}")

# Nombre de archivos
archivo_entrada = "entrada.txt"  # Debe estar en la misma carpeta
archivo_salida = "salida.txt"

generar_etiquetas(archivo_entrada, archivo_salida)