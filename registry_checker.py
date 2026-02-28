import winreg

def check_startup_registry():
    suspicious_entries = []

    try:
        registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path)

        i = 0
        while True:
            try:
                name, value, _ = winreg.EnumValue(key, i)
                suspicious_entries.append((name, value))
                i += 1
            except OSError:
                break

    except Exception:
        pass

    return suspicious_entries