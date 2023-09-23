```python
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

def main():
    while True:
        user_input = input("$ ")
        if user_input == "exit":
            break
        output, error = run_command(user_input)
        if output:
            print(output)
        if error:
            print(error)

if __name__ == "__main__":
    main()
```