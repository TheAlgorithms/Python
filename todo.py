import json
import os

# Define the file where tasks will be stored.
DATA_FILE = "tasks.json"

def load_tasks():
    """
    Loads tasks from the DATA_FILE.

    If the file does not exist, an empty list is returned.
    Handles potential JSON decoding errors or OS-related file errors.

    Returns:
        list: A list of dictionaries, where each dictionary represents a task.
              Returns an empty list if the file is not found or corrupted.
    """
    # Check if the data file exists. If not, there are no tasks to load yet.
    if not os.path.exists(DATA_FILE):
        return []
    try:
        # Open the file in read mode with UTF-8 encoding for broader character support.
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            # Load the JSON data from the file.
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        # Catch errors if the JSON is malformed or if there's an OS-related error
        # (e.g., permission denied, disk error during read).
        print(f"Error loading tasks: {e}. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    """
    Saves the current list of tasks to the DATA_FILE.

    Handles potential OS-related file errors during saving.

    Args:
        tasks (list): The list of task dictionaries to be saved.
    """
    try:
        # Open the file in write mode with UTF-8 encoding.
        # `ensure_ascii=False` allows non-ASCII characters (like emojis) to be saved directly.
        # `indent=2` formats the JSON for better readability.
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except OSError as e:
        # Catch errors if there's an OS-related error during write (e.g., permission denied, disk full).
        print(f"Error saving tasks: {e}. Your changes might not have been saved.")

def list_tasks(tasks):
    """
    Prints all tasks to the console, showing their status and index.

    Args:
        tasks (list): The list of task dictionaries to display.
    """
    if not tasks:
        print("No tasks to display.")
        return

    print("\n--- Your To-Do List ---")
    for i, t in enumerate(tasks, 1):
        # Determine the status symbol based on the 'done' flag.
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['title']}")
    print("-----------------------\n")

def add_task(tasks, title):
    """
    Adds a new task to the list.

    Args:
        tasks (list): The current list of task dictionaries.
        title (str): The title of the new task.
    """
    title = title.strip() # Remove leading/trailing whitespace
    if not title:
        print("Error: Task title cannot be empty.")
        return

    # Create a new task dictionary with a default 'done' status of False.
    tasks.append({"title": title, "done": False})
    save_tasks(tasks) # Save the updated list to file.
    print(f"Task '{title}' added successfully.")

def toggle_task(tasks, index_str):
    """
    Toggles the 'done' status of a task at the specified index.

    Args:
        tasks (list): The current list of task dictionaries.
        index_str (str): The string representation of the 1-based index of the task.
    """
    try:
        index = int(index_str)
    except ValueError:
        print(f"Error: Invalid task number '{index_str}'. Please enter a valid integer.")
        return

    # Adjust index to be 0-based for list access.
    # Validate the index to ensure it's within the bounds of the task list.
    if index < 1 or index > len(tasks):
        print(f"Error: Task number {index} is out of range. Please choose a number between 1 and {len(tasks) if tasks else 0}.")
        return

    # Toggle the 'done' status.
    tasks[index - 1]["done"] = not tasks[index - 1]["done"]
    save_tasks(tasks) # Save the updated list.
    status_msg = "completed" if tasks[index - 1]["done"] else "marked as not completed"
    print(f"Task {index} '{tasks[index-1]['title']}' {status_msg}.")

def delete_task(tasks, index_str):
    """
    Deletes a task from the list at the specified index.

    Args:
        tasks (list): The current list of task dictionaries.
        index_str (str): The string representation of the 1-based index of the task.
    """
    try:
        index = int(index_str)
    except ValueError:
        print(f"Error: Invalid task number '{index_str}'. Please enter a valid integer.")
        return

    # Adjust index to be 0-based for list access.
    # Validate the index.
    if index < 1 or index > len(tasks):
        print(f"Error: Task number {index} is out of range. Please choose a number between 1 and {len(tasks) if tasks else 0}.")
        return

    # Remove the task from the list and store its title for confirmation message.
    removed_task_title = tasks.pop(index - 1)["title"]
    save_tasks(tasks) # Save the updated list.
    print(f"Task {index} '{removed_task_title}' deleted successfully.")

def help_menu():
    """
    Displays the help menu with available commands.
    """
    print("\n--- Commands ---")
    print("  list                : Show all tasks.")
    print("  add <title>         : Add a new task with the given title.")
    print("  done <num>          : Toggle the completion status of task <num>.")
    print("  del <num>           : Delete task <num>.")
    print("  help                : Show this help message.")
    print("  quit                : Exit the application.")
    print("----------------\n")

def main():
    """
    The main function to run the To-Do List application.
    It loads tasks, enters a command loop, and processes user input.
    """
    tasks = load_tasks() # Load tasks at the start of the application.
    print("Welcome to the Simple To-Do List!")
    help_menu() # Display the help menu initially.

    while True:
        try:
            # Prompt the user for a command.
            cmd_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+D (EOFError) or Ctrl+C (KeyboardInterrupt) to exit gracefully.
            print("\nExiting To-Do List. Goodbye!")
            break

        # If the input is empty, just prompt again.
        if not cmd_input:
            continue

        # Split the command into action and arguments.
        parts = cmd_input.split(maxsplit=1)
        action = parts[0].lower() # Convert action to lowercase for case-insensitive comparison.

        if action == "list":
            list_tasks(tasks)
        elif action == "add":
            # Check if a title was provided for the 'add' command.
            if len(parts) < 2:
                print("Usage: add <title> (e.g., add Buy groceries)")
            else:
                add_task(tasks, parts[1])
        elif action == "done":
            # Check if a task number was provided and if it's a digit.
            if len(parts) < 2:
                print("Usage: done <num> (e.g., done 1)")
            else:
                toggle_task(tasks, parts[1])
        elif action == "del":
            # Check if a task number was provided and if it's a digit.
            if len(parts) < 2:
                print("Usage: del <num> (e.g., del 2)")
            else:
                delete_task(tasks, parts[1])
        elif action == "help":
            help_menu()
        elif action == "quit":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            # Inform the user about unknown commands.
            print(f"Unknown command: '{action}'. Type 'help' to see available commands.")

# Entry point for the script.
if __name__ == "__main__":
    main()
