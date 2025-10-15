try:
    # Get boy's name
    boyName = input("Boy Name : ")
    if not boyName or not boyName.strip():
        raise ValueError("Boy name cannot be empty")
    if not boyName.replace(" ", "").isalpha():
        raise TypeError("Boy name must contain only alphabetic characters")
    
    # Get boy's age
    boyAgeInput = input("Boy age : ")
    if not boyAgeInput.strip():
        raise ValueError("Boy age cannot be empty")
    try:
        boyAge = int(boyAgeInput)
        if boyAge <= 0:
            raise ValueError("Boy age must be a positive number")
    except ValueError as e:
        if "invalid literal" in str(e):
            raise TypeError("Boy age must be a valid integer")
        raise
    
    # Get girl's name
    girlName = input("Girl Name : ")
    if not girlName or not girlName.strip():
        raise ValueError("Girl name cannot be empty")
    if not girlName.replace(" ", "").isalpha():
        raise TypeError("Girl name must contain only alphabetic characters")
    
    # Get girl's age
    girlAgeInput = input("Girl age : ")
    if not girlAgeInput.strip():
        raise ValueError("Girl age cannot be empty")
    try:
        girlAge = int(girlAgeInput)
        if girlAge <= 0:
            raise ValueError("Girl age must be a positive number")
    except ValueError as e:
        if "invalid literal" in str(e):
            raise TypeError("Girl age must be a valid integer")
        raise
    
    # Calculate and display result
    print(boyName, "loves", girlName, ". Age difference is", abs(boyAge - girlAge))

except TypeError as e:
    print(f"Type Mismatch Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")