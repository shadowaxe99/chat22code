```python
import websocket
import json

class ChatInterface:
    def __init__(self):
        self.websocket = None

    def connect(self):
        self.websocket = websocket.create_connection("wss://api.openai.com/v1/chat/completions")

    def disconnect(self):
        self.websocket.close()

    def send_message(self, message):
        payload = {
            "type": "message",
            "content": message
        }
        self.websocket.send(json.dumps(payload))

    def receive_message(self):
        response = self.websocket.recv()
        return json.loads(response)

    def main_loop(self):
        self.connect()
        while True:
            user_input = input("User: ")
            self.send_message(user_input)
            response = self.receive_message()
            print("AI: " + response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    chat_interface = ChatInterface()
    chat_interface.main_loop()
```

This is the code for the `chat_interface.py` file. It defines a `ChatInterface` class that handles the WebSocket connection with the OpenAI GPT API for real-time chat interactions. The `connect` method establishes the WebSocket connection, the `disconnect` method closes the connection, the `send_message` method sends a message to the API, and the `receive_message` method receives a response from the API. The `main_loop` method continuously prompts the user for input, sends it to the API, and prints the AI's response.

To use this code, you need to have the `websocket` library installed. You can install it using `pip install websocket-client`.