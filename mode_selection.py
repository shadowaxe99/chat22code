```python
class ModeSelection:
    def __init__(self):
        self.mode = "Chat Only"

    def toggle_mode(self):
        if self.mode == "Chat Only":
            self.mode = "Code"
        else:
            self.mode = "Chat Only"

    def get_mode(self):
        return self.mode
```
