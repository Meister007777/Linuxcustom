import subprocess
import sys

def main():
    # Nutzt das erste Argument als Commit-Nachricht, sonst einen Standardtext
    msg = sys.argv[1] if len(sys.argv) > 1 else "Dotfiles aktualisiert"
    
    try:
        # Führt die 3 Git-Befehle nacheinander aus
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Erfolgreich auf GitHub hochgeladen!")
    except subprocess.CalledProcessError:
        print("Fehler: Git-Befehl fehlgeschlagen.")

if __name__ == "__main__":
    main()
