from os import system
system("chmod 777 qr.py")
import qrcode  # Importamos el modulo necesario para trabajar con codigos QR
system("clear")

system("rm -r Imagen")
print("\033[1;31mby: DemoEC")
print("\033[1;36m")
print(" ______________________________________")
print("|   ___            _        __         |")
print("|  / _ \ _ __     (_)_ __  / _| ___    |")
print("| | | | | '__|____| | '_ \| |_ / _ \   |")
print("| | |_| | | |_____| | | | |  _| (_) |  |")
print("|  \__\_\_|       |_|_| |_|_|  \___/   |")
print("|______________________________________|")
print("")
print("")
informacion = input("\033[1;31m[\033[1;37m+\033[1;31m]\033[1;32mIngrese una direccion web,numero,msj : \033[1;34m")
print("\033[1;31m[\033[1;37m+\033[1;31m]\033[1;32mNombre del archivo : \033[1;34mQr.png")
print("")
system("sleep 3")

img = qrcode.make(informacion)  # Creamos un codigo a partir de una cadena de texto

archivo_imagen = open('Qr.png', 'wb')
img.save(archivo_imagen)
archivo_imagen.close()
print("\033[1;37m---------------------------------------------------------")
print(f"|\033[1;32mSe ha guardado la informacion en formato \033[1;34m/Imagen/Qr.png\033[1;37m|")
print("\033[1;37m---------------------------------------------------------")
system("mkdir Imagen")
system("mv Qr.png Imagen")

