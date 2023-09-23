```python
import psutil

def monitor_performance():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")
    print(f"Disk Usage: {disk_percent}%")

monitor_performance()
```
This code snippet demonstrates how to monitor the performance of the system using the `psutil` library in Python. It retrieves the CPU usage, memory usage, and disk usage percentages and prints them to the console. You can integrate this code into your performance monitoring feature to provide real-time resource usage information to the user.