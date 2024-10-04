"""
Example to show how this method works

>>> swap_case ("Hello")
hELLO

>>> swap_case ("water")
WATER
"""


def swap_case(input_string) -> str:
    """This method will swap the cases of a given string
    eg: input: input_string= "Hello" output: swapped_string="hELLO" """
    list_representation = list(input_string)
    for i in range(len(list_representation)):
        if list_representation[i] >= "A" and list_representation[i] <= "Z":
            m2 = ord(list_representation[i])
            m1 = m2 + 32
            list_representation[i] = chr(m1)
        elif list_representation[i] >= "a" and list_representation[i] <= "z":
            m3 = ord(list_representation[i])
            m4 = m3 - 32
            list_representation[i] = chr(m4)
        else:
            pass
    swapped_list = "".join(list_representation)
    return swapped_list

#sample test case
input_string = "Hello"
swapped_string = swap_case(input_string)
print(swapped_string)
