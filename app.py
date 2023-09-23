```python
import os
import subprocess

def display_terminal():
    # Display the native MacOS terminal in half of the application window
    subprocess.call(["open", "-a", "Terminal"])

def display_chat_interface():
    # Display the chat interface in the other half of the application window
    # TODO: Implement chat interface
    pass

def select_model(model):
    # Allow users to choose between different OpenAI GPT models
    # TODO: Implement model selection
    pass

def start_new_session():
    # Enable users to start new chat sessions
    # TODO: Implement new session functionality
    pass

def view_chat_history():
    # Enable users to view past chat history
    # TODO: Implement chat history functionality
    pass

def display_token_count():
    # Display token count for the current chat and individual messages
    # TODO: Implement token count display
    pass

def toggle_mode(mode):
    # Enable users to toggle between "Chat Only" and "Code" modes
    # TODO: Implement mode selection
    pass

def handle_user_input(user_input):
    # Handle user input and perform appropriate actions
    # TODO: Implement user input handling
    pass

def main():
    # Main function to run the application
    display_terminal()
    display_chat_interface()

    while True:
        user_input = input("Enter a command: ")
        handle_user_input(user_input)

if __name__ == "__main__":
    main()
```

This is the code for the `app.py` file. It includes the main function that runs the application, as well as placeholder functions for the different features and specifications mentioned in the overview. Each function is marked with a `TODO` comment to indicate that the implementation is pending. You can fill in the implementation details for each function according to your requirements.