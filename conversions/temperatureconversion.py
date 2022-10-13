"""
This Python code converts Centigrade to Fahrenheit
Or Fahrenheit to Centigrate

You need to give input in Celcius or Farenheit.
For example:- 45F , 102C ,etc.
"""
def tempConvert():
    temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
    degree = int(temp[:-1])
    i_convention = temp[-1]

    if i_convention.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        o_convention = "Fahrenheit"
    elif i_convention.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        o_convent4ion = "Celsius"
    else:
        print("Input proper convention.")
        quit()
    print("The temperature in", o_convention, "is", result, "degrees.")

if __name__ == "__main__":
    tempConvert()