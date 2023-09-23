```python
import os
import subprocess

def send_notification(title, message):
    command = f'display notification "{message}" with title "{title}"'
    subprocess.call(['osascript', '-e', command])

def main():
    title = "Task Completed"
    message = "Your task has been completed successfully."
    send_notification(title, message)

if __name__ == "__main__":
    main()
```

This is the code for the `notifications.py` file. It defines a `send_notification` function that uses the `osascript` command to display a desktop notification on macOS. The `main` function demonstrates how to use the `send_notification` function to send a notification with a title and message.