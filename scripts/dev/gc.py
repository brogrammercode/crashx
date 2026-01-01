"""
GIT COMMIT AUTOMATED
"""

import subprocess

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def git_automate():
    try:
        # 1. ADD
        print(f"{Colors.YELLOW}Wait... Adding your changes to git...{Colors.RESET}")
        subprocess.run(['git', 'add', '.'], check=True)
        print(f"{Colors.GREEN}✔ Your changes have been added to git{Colors.RESET}\n")
        
        # 2. INPUT
        commit_message = input(f"{Colors.BOLD}{Colors.CYAN}Enter your commit message: {Colors.RESET}")

        if not commit_message:
            print(f"{Colors.RED}❌ Commit message cannot be empty{Colors.RESET}")
            return

        # 3. COMMIT
        print(f"\n{Colors.YELLOW}Wait... Committing your changes to git...{Colors.RESET}")
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"{Colors.GREEN}✔ Your changes have been committed to git{Colors.RESET}")
        
        # 4. PUSH (Commented out as per your script)
        print(f"\n{Colors.YELLOW}Pushing your changes to git...{Colors.RESET}")
        subprocess.run(['git', 'push'], check=True)
        print(f"{Colors.GREEN}✔ Your changes have been pushed to git{Colors.RESET}")

    except subprocess.CalledProcessError as e:
        # This catches errors if git fails (e.g., merge conflicts)
        print(f"\n{Colors.RED}❌ An error occurred: {e}{Colors.RESET}")

if __name__ == "__main__":
    git_automate()