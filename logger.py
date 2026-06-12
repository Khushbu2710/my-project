import subprocess
from datetime import datetime

def run_monitor(log_file="health_log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = subprocess.run(['python3', 'system_monitor.py'], capture_output=True, text=True)

    with open(log_file, 'a') as f:
        f.write(f"\n=== Log Entry: {timestamp} ===\n")
        f.write(result.stdout)

if __name__ == "__main__":
    run_monitor()
