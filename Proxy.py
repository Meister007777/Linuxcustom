import subprocess
import sys

if len(sys.argv) < 2:
    print("Es wird eine Ipv4 erwartet")
    sys.exit(1)

server_ip = sys.argv[1]
key_pfad = "~/.ssh/id_ed25519"

ssh_command = [
    "ssh",
    "-i", key_pfad,
    "-D", "1080",
    "-N", "-f",
    f"root@{server_ip}"
]
try:
    subprocess.run(ssh_command, check=True)
    print("SSH-Tunnel Erfolgreich {server_ip}:1080")
except subprocess.CalledProcessError:
    print("Fehler beim starten")