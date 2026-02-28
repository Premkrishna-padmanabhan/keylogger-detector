import time
from colorama import Fore, init
from process_monitor import get_running_processes
from signature_checker import is_suspicious
from registry_checker import check_startup_registry
from logger import log_alert

init()

def scan_processes():
    processes = get_running_processes()

    for process in processes:
        if is_suspicious(process):
            alert = f"[ALERT] Suspicious Process: {process}"
            print(Fore.RED + alert)
            log_alert(alert)

def scan_registry():
    entries = check_startup_registry()

    for name, value in entries:
        if "keylog" in value.lower():
            alert = f"[ALERT] Suspicious Startup Entry: {name} -> {value}"
            print(Fore.YELLOW + alert)
            log_alert(alert)

def main():
    print("🔍 Keylogger Detection Tool Started...\n")

    while True:
        scan_processes()
        scan_registry()
        time.sleep(15)

if __name__ == "__main__":
    main()