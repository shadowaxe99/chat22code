```python
class ChatHistory:
    def __init__(self):
        self.sessions = []

    def start_new_session(self):
        session = []
        self.sessions.append(session)

    def add_message(self, session_index, message):
        session = self.sessions[session_index]
        session.append(message)

    def get_session_history(self, session_index):
        return self.sessions[session_index]
```
