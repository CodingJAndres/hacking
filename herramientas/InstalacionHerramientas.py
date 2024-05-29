import subprocess
from colorama import init, Fore

# Inicializar colorama para colores en la terminal
init(autoreset=True)

# Función para instalar una herramienta
def install_tool(tool):
    print(Fore.YELLOW + f"Instalando {tool}...")
    subprocess.run(["sudo", "apt-get", "install", "-y", tool])

# Función para mostrar el menú de herramientas
def show_menu():
    print("\nBienvenido al instalador de herramientas de hacking ético")
    print("Seleccione una herramienta para instalar:")
    print("1. " + Fore.CYAN + "Nmap")
    print("2. " + Fore.CYAN + "Metasploit")
    print("3. " + Fore.CYAN + "Wireshark")
    print("4. " + Fore.CYAN + "Burp Suite")
    print("5. " + Fore.CYAN + "John the Ripper")
    print("6. " + Fore.CYAN + "Hydra")
    print("7. " + Fore.CYAN + "Aircrack-ng")
    print("8. " + Fore.CYAN + "SQLMap")
    print("9. " + Fore.CYAN + "Hashcat")
    print("10. " + Fore.CYAN + "Netcat")
    print("11. " + Fore.CYAN + "Ettercap")
    print("12. " + Fore.CYAN + "Scapy")
    print("0. " + Fore.RED + "Salir")

# Función para mostrar el menú después de instalar una herramienta
def post_install_menu(tool):
    print("\n¿Qué quieres hacer ahora?")
    print("1. Instalar más herramientas")
    print("0. Salir")
    choice = input("Ingrese su elección: ")

    if choice == '1':
        return True  # Indica que queremos permanecer en este menú
    elif choice == '0':
        print("¡Hasta luego!")
        return False  # Indica que queremos salir del programa
    else:
        print(Fore.RED + "Opción inválida")
        return False  # Indica que queremos permanecer en este menú

# Función principal
def main():
    while True:
        show_menu()
        choice = input("Ingrese el número de la herramienta que desea instalar: ")

        # Mapeo de herramientas a funciones de instalación
        tools = {
            '1': 'nmap',
            '2': 'metasploit',
            '3': 'wireshark',
            '4': 'burp-suite',
            '5': 'john',
            '6': 'hydra',
            '7': 'aircrack-ng',
            '8': 'sqlmap',
            '9': 'hashcat',
            '10': 'netcat',
            '11': 'ettercap',
            '12': 'scapy'
        }

        # Verificar si el usuario quiere salir
        if choice == '0':
            print("¡Hasta luego!")
            break

        # Verificar si la opción ingresada es válida
        elif choice in tools:
            install_tool(tools[choice])
            if not post_install_menu(tools[choice]):
                break  # Salir del bucle si el usuario elige salir
        else:
            print(Fore.RED + "Opción inválida")

if __name__ == "__main__":
    main()
