import subprocess
import ctypes
import sys
import time

def is_admin():

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():

    while True:
        cmd = 'sc query VeyonService'
        result = subprocess.run(cmd, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

        if "RUNNING" in result.stdout:
            print(f"De service is actief.")
            stop_cmd = 'sc stop VeyonService'
            stop_result = subprocess.run(stop_cmd, shell=True, capture_output=True, text=True)
            
            if stop_result.returncode == 0:
                print("Gestopt")
            else:
                print(f"Kon de service niet stoppen. Fout: {stop_result.stdout}")

        

        time.sleep(5)

if __name__ == "__main__":
    if is_admin():
        main()  # <--- Run main() in a separate thread
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

