import psutil

def get_running_processes():
    process_list = []

    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent']):
        try:
            process_list.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return process_list