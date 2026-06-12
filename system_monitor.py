import psutil

def main():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("===== SERVER HEALTH REPORT =====")
    print(f"CPU Usage    : {cpu}%")
    print(f"Memory Usage : {mem.percent}% ({mem.used // (1024**2)} MB used / {mem.total // (1024**2)} MB total)")
    print(f"Disk Usage   : {disk.percent}% ({disk.used // (1024**3)} GB used / {disk.total // (1024**3)} GB total)")
    print("=================================")

if __name__ == "__main__":
    main()
