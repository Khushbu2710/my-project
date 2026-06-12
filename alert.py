import psutil

CPU_THRESHOLD = 80
RAM_THRESHOLD = 80

def check_resources():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()

    if cpu > CPU_THRESHOLD:
        print(f"WARNING: High CPU usage: {cpu}%")
    else:
        print(f"CPU usage OK: {cpu}%")

    if mem.percent > RAM_THRESHOLD:
        print(f"WARNING: High RAM usage: {mem.percent}%")
    else:
        print(f"RAM usage OK: {mem.percent}%")

if __name__ == "__main__":
    check_resources()
