#!/usr/bin/env python3
import pyfiglet
import sys

# Farben für das Terminal definieren
GREEN = "\033[1;32m"
RESET = "\033[0m"

# Funktion für das Banner
def print_banner(text):
    banner = pyfiglet.figlet_format(text, font="slant")
    print(f"{GREEN}{banner}{RESET}")

# Argumente auswerten
if len(sys.argv) == 1:

    print_banner("Commands")
    print_banner("- Apps")
    print_banner("- shortcuts")
    print_banner("- Tools")
else:
    # Argumente zu einem Text zusammenfügen
    user_input = " ".join(sys.argv[1:])
    
    # Befehle prüfen
    if user_input == "Apps":
        print_banner("osu")
    elif user_input == "shortcuts":
        print_banner("zsh")
        print_banner("szsh")
        print_banner("gsync")
    elif user_input == "Tools":
        print_banner("Proxy %ipv4%")
        print_banner("tmole %port%")
    else:
        print_banner(f"Unbekannter Befehl: {user_input}")
