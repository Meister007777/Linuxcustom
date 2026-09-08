#!/usr/bin/env python3
import pyfiglet
import sys

# Define terminal colors
GREEN = "\033[1;32m"
RESET = "\033[0m"

# Function to render the banner
def print_banner(text):
    banner = pyfiglet.figlet_format(text, font="slant")
    print(f"{GREEN}{banner}{RESET}")

# Evaluate CLI arguments
if len(sys.argv) == 1:
    print_banner("Commands")
    print_banner("- Apps")
    print_banner("- Shortcuts")
    print_banner("- Tools")
else:
    # Combine arguments into a single string
    user_input = " ".join(sys.argv[1:])
    
    # Check commands
    if user_input == "Apps":
        print_banner("osu")
    elif user_input == "shortcuts" or user_input == "Shortcuts":
        print_banner("zsh")
        print_banner("szsh")
        print_banner("gsync")
    elif user_input == "Tools":
        print_banner("Proxy %ipv4%")
        print_banner("tmole %port%")
    else:
        print_banner(f"Unknown Command: {user_input}")
