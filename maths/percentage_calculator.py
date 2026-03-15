def calculate_percentage(value, percent):
    return (value * percent) / 100


value = float(input("Enter value: "))
percent = float(input("Enter percentage: "))

result = calculate_percentage(value, percent)

print("Result:", result)