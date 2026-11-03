def greet(name: str) -> str:
    """Return a greeting message.

    >>> greet("Student")
    'Hello, Student!'
    """
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet("Student"))
