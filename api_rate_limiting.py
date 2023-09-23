```python
import time

class RateLimiter:
    def __init__(self, max_requests, interval):
        self.max_requests = max_requests
        self.interval = interval
        self.requests = []
    
    def can_make_request(self):
        current_time = time.time()
        self.requests = [request for request in self.requests if request > current_time - self.interval]
        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False
```

This is a basic implementation of an API rate limiter in Python. The `RateLimiter` class allows you to set a maximum number of requests (`max_requests`) within a given time interval (`interval`). The `can_make_request` method checks if a new request can be made based on the current number of requests and the time interval. If the maximum number of requests has not been reached, a new request is allowed and the current time is added to the list of requests. Otherwise, the request is denied.

You can customize the `max_requests` and `interval` values according to your specific rate limiting requirements.