```python
import threading
import time

class TaskHandler:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()

    def add_task(self, task):
        with self.lock:
            self.tasks.append(task)

    def process_tasks(self):
        while True:
            with self.lock:
                if len(self.tasks) == 0:
                    break
                task = self.tasks.pop(0)
            # Process the task here
            print(f"Processing task: {task}")
            time.sleep(1)  # Simulating task processing time

# Example usage
task_handler = TaskHandler()
task_handler.add_task("Task 1")
task_handler.add_task("Task 2")
task_handler.add_task("Task 3")

# Start processing tasks in a separate thread
task_thread = threading.Thread(target=task_handler.process_tasks)
task_thread.start()

# Wait for the task thread to finish
task_thread.join()
```

This is a basic implementation of a `TaskHandler` class that allows adding tasks and processing them in a separate thread. The `TaskHandler` class has a `tasks` list to store the tasks and a `lock` to ensure thread safety when accessing the list.

The `add_task` method is used to add tasks to the `tasks` list. The `process_tasks` method continuously checks for tasks in the `tasks` list and processes them one by one. In this example, the processing of a task is simulated by printing the task and sleeping for 1 second.

To use the `TaskHandler`, you can create an instance of it (`task_handler`) and add tasks using the `add_task` method. Then, you can start processing the tasks in a separate thread by creating a `Thread` object (`task_thread`) and passing the `process_tasks` method as the target. Finally, you can wait for the task thread to finish using the `join` method.

Note that this is a simplified example and you may need to modify the `TaskHandler` class to suit your specific requirements.