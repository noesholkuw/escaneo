import nmap

def escanear_puertos(ip, rango_puertos):
    scanner = nmap.PortScanner()

    # Escanea los puertos especificados en el rango
    scanner.scan(ip, rango_puertos)

    # Obtiene los resultados del escaneo
    resultados = scanner[ip]

    print(f"Escaneo de puertos para {ip}:\n")

    for puerto, info in resultados["tcp"].items():
        estado = info["state"]
        servicio = info["name"] if "name" in info else "Desconocido"
        print(f"Puerto {puerto}: {estado}, Servicio: {servicio}")

if __name__ == "__main__":
    direccion_ip = input("Ingresa la dirección IP a escanear: ")
    rango_puertos = input("Ingresa el rango de puertos a escanear (ejemplo: 1-1000): ")

    escanear_puertos(direccion_ip, rango_puertos)