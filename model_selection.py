# model_selection.py

```python
import tkinter as tk
from tkinter import ttk

class ModelSelectionWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Model Selection")
        self.geometry("300x200")
        self.resizable(False, False)
        
        self.model_var = tk.StringVar()
        self.model_var.set("GPT-3.5")
        
        self.model_label = ttk.Label(self, text="Select Model:")
        self.model_label.pack(pady=10)
        
        self.model_combobox = ttk.Combobox(self, textvariable=self.model_var, values=["GPT-3.5", "GPT-4", "Claude"])
        self.model_combobox.pack(pady=10)
        
        self.ok_button = ttk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def on_ok(self):
        selected_model = self.model_var.get()
        print(f"Selected Model: {selected_model}")
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    model_selection_window = ModelSelectionWindow(root)
    root.mainloop()
```

This code generates a `ModelSelectionWindow` class that creates a pop-up window for selecting the GPT model. The window contains a label, a combobox with options for GPT-3.5, GPT-4, and Claude, and an OK button. When the OK button is clicked, the selected model is printed to the console. The code also includes a test section that creates an instance of `ModelSelectionWindow` and runs the tkinter event loop.