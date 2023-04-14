import psutil
import datetime
import time

LOG_FILE = '/var/log/system_monitor.log'
MAX_LOG_FILE_SIZE = 500 * 1024 * 1024  # 500 MB

def monitor_system():
    while True:
        with open(LOG_FILE, 'a') as f:
            now = datetime.datetime.now()
            cpu_percent = psutil.cpu_percent()
            mem_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage('/')
            log_line = f'{now}\tCPU: {cpu_percent}%\tMemory: {mem_info.percent}%\tDisk: {disk_info.percent}%\n'
            f.write(log_line)
        
        # Check log file size and overwrite if necessary
        if os.path.getsize(LOG_FILE) > MAX_LOG_FILE_SIZE:
            with open(LOG_FILE, 'w') as f:
                f.write('')
        
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == '__main__':
    monitor_system()
