# offline_mode.py

```python
class OfflineMode:
    def __init__(self):
        self.enabled = False

    def enable_offline_mode(self):
        self.enabled = True

    def disable_offline_mode(self):
        self.enabled = False

    def is_offline_mode_enabled(self):
        return self.enabled
```

This is the code for the `OfflineMode` class in the `offline_mode.py` file. The class provides functionality to enable and disable offline mode in the application. The `OfflineMode` class has three methods:

- `enable_offline_mode()`: This method enables the offline mode by setting the `enabled` attribute to `True`.
- `disable_offline_mode()`: This method disables the offline mode by setting the `enabled` attribute to `False`.
- `is_offline_mode_enabled()`: This method returns the current status of the offline mode (`True` if enabled, `False` if disabled).

The `OfflineMode` class is responsible for managing the limited functionality when the application is offline.