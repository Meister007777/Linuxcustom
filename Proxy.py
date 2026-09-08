import subprocess
import sys
import pyfiglet

if len(sys.argv) < 2:
    print("Error: An IPv4 address is required.")
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
    print(f"SSH Tunnel successfully established at {server_ip}:1080")
except subprocess.CalledProcessError:
    print("Error: Failed to start the SSH tunnel.")
