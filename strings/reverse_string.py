# We can reverse a string with indexing
txt = 'This is a sample text' # Making a text for reversing
reversed_text = txt[::-1] # This slicing is starting from the end and going backward
print(reversed_text)

# With a function
def text_reversing(text):
    reversed_text = text[::-1] # Storing the reversed text in a variable
    return reversed_text # Returning the reversed text variable

result = text_reversing('Hi, How are you?') # Giving the function the text as parameter
print(result) # Printing the reversed text