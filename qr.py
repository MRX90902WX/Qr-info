from os import system
system("bash sys.sh")
import qrcode  # Importamos el modulo necesario para trabajar con codigos QR
system("clear")

system("setterm -foreground green")
print("  ___         _        __")
print(" / _ \ _ __  (_)_ __  / _| ___")
print("| | | | '__| | | '_ \| |_ / _ \ ")
print("| |_| | |    | | | | |  _| (_) |")
print(" \__\_\_|    |_|_| |_|_|  \___/")
print(" ")
print(" ")

a = input("[+]Ingrese una direccion web o cell , msj: ")
print(" ")
print("Cargando ...")
system("sleep 3")

img = qrcode.make(a)  # Creamos un codigo a partir de una cadena de texto

archivo_imagen = open('codigo.png', 'wb')
img.save(archivo_imagen)
archivo_imagen.close()
print("----------------------------------------------------------")
print(f"Se ha guardado {a} en su codigo.png")
print("----------------------------------------------------------")
