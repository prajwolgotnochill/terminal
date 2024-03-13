import subprocess

def connect_to_bash_shell():
    try:
        subprocess.call("bash", shell=True)
    except FileNotFoundError:
        print("Error: Bash shell not found.")

if __name__ == "__main__":
    print("Connecting to Bash shell...")
    connect_to_bash_shell()
