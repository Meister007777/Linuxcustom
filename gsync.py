import subprocess
import sys
import os

def main():
    dotfiles_path = os.path.expanduser("~/dotfiles")
    
    try:
        os.chdir(dotfiles_path)
    except FileNotFoundError:
        print(f"Fehler: Der Ordner {dotfiles_path} existiert nicht.")
        return

    # 1. Git add ausführen, um den aktuellen Status zu erfassen
    subprocess.run(["git", "add", "."], check=True)

    # 2. Prüfen, ob es überhaupt Änderungen zum Committen gibt
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not status.stdout.strip():
        print("Es gibt keine neuen Änderungen zum Hochladen.")
        return

    # 3. Commit-Nachricht holen
    msg = sys.argv if len(sys.argv) > 1 else "Dotfiles aktualisiert"
    
    # 4. Commit und Push ausführen
    try:
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Erfolgreich auf GitHub hochgeladen!")
    except subprocess.CalledProcessError:
        print("Fehler: Git-Befehl fehlgeschlagen.")

if __name__ == "__main__":
    main()
