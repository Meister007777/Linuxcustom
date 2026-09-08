import subprocess
import sys
import os

def main():
    dotfiles_path = os.path.expanduser("~/dotfiles")
    
    try:
        os.chdir(dotfiles_path)
    except FileNotFoundError:
        print(f"Error: The directory {dotfiles_path} does not exist.")
        return

    # 1. Execute git add to stage current changes
    subprocess.run(["git", "add", "."], check=True)

    # 2. Check if there are any changes to commit
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not status.stdout.strip():
        print("No new changes detected to upload.")
        return

    # 3. Get commit message
    msg = sys.argv[1] if len(sys.argv) > 1 else "Dotfiles updated"
    
    # 4. Execute commit and push
    try:
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully uploaded to GitHub!")
    except subprocess.CalledProcessError:
        print("Error: Git command failed.")

if __name__ == "__main__":
    main()
