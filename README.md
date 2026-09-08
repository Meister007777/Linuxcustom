# Linuxcustom
# Kali Linux Environment Automation & Dotfiles Management

A centralized repository containing system configurations, Zsh environment initializers, and custom automation utilities tailored for a secure Kali Linux workspace.

## Repository Structure

* `.zshrc` — Core Zsh configuration file utilizing the Oh My Zsh framework.
* `Start.py` — The central CLI navigation hub and visual command overview utility.
* `Proxy.py` — Automated SSH dynamic SOCKS5 proxy tunnel script.
* `gsync.py` — Zsh-aliased CLI tool for automated Git staging, committing, and pushing.

---

## Component Overview

### 1. Zsh Environment Configuration (`.zshrc`)
The foundational configuration script managing shell behavior, environmental paths, and custom system abstractions.
* **Framework:** Powered by Oh My Zsh leveraging the `duellj` theme framework.
* **Aliasing:** Map local scripts and directories directly to terminal commands (`menu`, `gsync`, `Proxy`, `osu`) to accelerate administration workflows.
* **Initialization Pipeline:** Triggers system telemetry (`fastfetch`), dynamic banner generation (`toilet`), and interactive option routing immediately upon shell creation.

### 2. Central CLI Command Menu (`Start.py`)
An interactive, ASCII-art-driven terminal interface designed to visually organize and reference custom system paths, Zsh shortcuts, and network tools.
* **Visual Styling:** Utilizes `pyfiglet` for dynamic ASCII banners and ANSI escape codes for high-visibility green terminal formatting.
* **Argument-Driven Logic:** Filters and displays categories (`Apps`, `shortcuts`, `Tools`) based on CLI input arguments.

### 3. SSH Dynamic Proxy Tunnel (`Proxy.py`)
A Python utility designed to establish an encrypted SOCKS5 proxy tunnel via SSH for secure routing and network traffic obfuscation.
* **Dynamic Forwarding:** Automatically initializes a local proxy on port `1080` (`-D 1080`).
* **Background Operation:** Executes seamlessly without occupying a remote terminal shell (`-N -f`).
* **Secure Authentication:** Integrates with native ED25519 SSH keys located at `~/.ssh/id_ed25519`.

### 4. GitAutoPush CLI (`gsync.py`)
An automation script tailored for dotfiles environments to streamline Git version control workflows for local configuration tracking.
* **Smart Detection:** Implements `git status --porcelain` to verify the existence of modifications before initiating a commit, preventing empty repository updates.
* **Error Resilience:** Features dedicated exception handling (`FileNotFoundError`, `CalledProcessError`) to guarantee operational stability.

---

## Technical Requirements & Execution

### Prerequisites
* Kali Linux environment with Git, Zsh, and Oh My Zsh installed
* System utilities: `fastfetch`, `cmatrix`, `toilet`
* Python 3.x
* External Python dependencies:
  ```zsh
  pip install pyfiglet
  ```

### Integration & Aliases
The scripts are mapped within the environment using the following Zsh configurations:
```zsh
alias menu="~/dotfiles/Start.py"
alias gsync="cd ~/dotfiles && python3 ~/dotfiles/gsync.py"
alias Proxy="cd ~/dotfiles && python3 ~/dotfiles/Proxy.py"
```

### Execution Examples
1. **Accessing the tools category:**
   ```zsh
   menu Tools
   ```
2. **Initializing the secure SSH proxy tunnel:**
   ```zsh
   Proxy <target_ipv4_address>
   ```
3. **Triggering automated environment synchronization:**
   ```zsh
   gsync "Feat: optimized alias structure in zshrc"
   ```
