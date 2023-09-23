```python
import requests

def send_response_to_web_endpoint(response):
    endpoint_url = "https://example.com/api"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "response": response
    }
    response = requests.post(endpoint_url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Response sent successfully to web endpoint.")
    else:
        print("Failed to send response to web endpoint.")
```
