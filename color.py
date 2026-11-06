from colorama import Fore, Style

#Kirjuta programm, mis küsib kasutajalt tema lemmikvärvi ja väljastab selle põhjal tema temperamendi.

#punane --> energiline
#roosa --> romantik
#roheline --> rahulik
#sinine --> keskendunud
#must --> rokib täiega
#muu --> imeline ükssarvik

# color = input("Sisesta oma lemmikvärv:").lower() 

# """ if color == "punane":
#     print("Sa oled energeline inimene!")
# elif color == "roosa":
#     print("Sa oled romantik!")
# elif color == "roheline":
#     print("Sa oled rahulik inimene!")
# elif color == "must":
#     print("Sa rokid täiega!")
# elif color == "sinine":
#     print("Sa oled keskendunud inimene!")
# else:
#     print("Sa oled imeline ükssarvik!") """

# color = input("Sisesta oma lemmikvärv:").lower() 

# match color:
#     case "punane":
#         print("Sa oled energeline inimene!")
#     case "roosa":
#         print("Sa oled romantik!")
#     case "roheline":
#         print("Sa oled rahulik inimene!")
#     case "sinine":
#         print("Sa oled keskendunud inimene!")
#     case "must":
#         print("Sa rokid täiega!")
#     case _:
#         print("Sa oled imeline ükssarvik!")

color = input("Sisesta oma lemmikvärv:").lower()

match color:
    case "punane":
        print(Fore.RED + "Sa oled energeline inimene!" + Style.RESET_ALL)
    case "roosa":
        print(Fore.MAGENTA + "Sa oled romantik!" + Style.RESET_ALL)
    case "roheline":
        print(Fore.GREEN + "Sa oled rahulik inimene!" + Style.RESET_ALL)
    case "sinine":
        print(Fore.BLUE + "Sa oled keskendunud inimene!" + Style.RESET_ALL)
    case "must":
        print(Fore.BLACK + "Sa rokid täiega!" + Style.RESET_ALL)
    case "kollane":
            print(Fore.YELLOW + "Sa oled võilill!" + Style.RESET_ALL)
    case _:
            print(Fore.CYAN + "Sa oled imeline ükssarvik!" + Style.RESET_ALL)