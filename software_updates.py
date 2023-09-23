```python
import auto_update_library
import version_control

def check_for_updates():
    current_version = auto_update_library.get_current_version()
    latest_version = auto_update_library.get_latest_version()

    if latest_version > current_version:
        update_available = True
        update_message = f"An update is available! You are currently using version {current_version}, and the latest version is {latest_version}."
    else:
        update_available = False
        update_message = "You are using the latest version of the software."

    return update_available, update_message

def update_software():
    update_successful = auto_update_library.update()
    if update_successful:
        return "Software update successful."
    else:
        return "Software update failed. Please try again later."

def get_update_history():
    return version_control.get_commit_history()

def display_update_notification():
    auto_update_library.display_notification("Software update available", "An update is available for the software. Click here to update.")

if __name__ == "__main__":
    update_available, update_message = check_for_updates()
    print(update_message)

    if update_available:
        update_successful = update_software()
        print(update_successful)

    commit_history = get_update_history()
    print(commit_history)
```
