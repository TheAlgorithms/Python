def greet_user(name: str) -> str:
    """Return a greeting for the given user."""
    return f"Hello, {name}! Welcome to our project."


if __name__ == "__main__":
    print(greet_user("Student"))
    print(greet_user("Alex"))
