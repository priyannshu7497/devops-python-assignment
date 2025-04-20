import psutil
import time

# Threshold for alert
CPU_THRESHOLD = 80  # in percent
CHECK_INTERVAL = 1  # in seconds

def monitor_cpu():
    print("Monitoring CPU usage...\nPress Ctrl+C to stop.\n")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu_usage}%")

            if cpu_usage > CPU_THRESHOLD:
                print(f" Alert! CPU usage exceeds threshold: {cpu_usage}%")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")
    except Exception as e:
        print(f" Error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()
