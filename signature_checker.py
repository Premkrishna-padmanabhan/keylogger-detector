SUSPICIOUS_KEYWORDS = [
    "keylog",
    "hook",
    "keyboard",
    "logger",
    "capture"
]

def is_suspicious(process):
    name = str(process.get("name", "")).lower()
    exe = str(process.get("exe", "")).lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in name or keyword in exe:
            return True

    return False