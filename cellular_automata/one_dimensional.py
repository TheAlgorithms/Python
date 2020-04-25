from PIL import Image
'''
Returns an image of 16 generations of
one-dimensional cellular automata 
based on a given ruleset number
https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
'''
def format_ruleset(ruleset: int) -> list:
    '''
    >>> format_ruleset(11100)
    [0, 0, 0, 1, 1, 1, 0, 0]
    >>> format_ruleset(0)
    [0, 0, 0, 0, 0, 0, 0, 0]
    >>> format_ruleset(11111111)
    [1, 1, 1, 1, 1, 1, 1, 1]
    '''
    return [int(c) for c in f"{ruleset:08}"[:8]]

# Defines the first generation of cells

CELLS = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]]

# Mainloop

def new_generation(CELLS,RULE,time):
    new_row = []

    for i in range(31):

        # Gets neighbors of a cell

        # If leftmost cell is in consideration

        if i == 0:
            left_neighbor = 0
            right_neighbor = CELLS[time][i + 1]
        elif i == 30:

        # If rightmost cell is in consideration

            left_neighbor = CELLS[time][i - 1]
            right_neighbor = 0
        else:

        # All other cells

            left_neighbor = CELLS[time][i - 1]
            right_neighbor = CELLS[time][i + 1]

        # Defines new cell in and adds it to the new generation

        SITUATION = 7 - int(str(left_neighbor) + str(CELLS[time][i])
                            + str(right_neighbor), 2)
        new_row.append(RULE[SITUATION])
    #returns new generation
    return new_row

def generate_image(CELLS: list) -> Image:
    """
    Convert the cells into a PIL.Image.Image and return it to the caller.
    >>> from random import randint
    >>> cells = [[randint(0, 1) for w in range(31)] for h in range(16)]
    >>> img = generate_image(cells)
    >>> isinstance(img, PIL.Image.Image)
    True
    >>> img.size
    (31, 16)
    """
    # Creates the outputting image

    RESULT = Image.new('RGB', (31, 16))
    PIXELS = RESULT.load()

    # Generates image
    for w in range(31):
        for h in range(16):
            color = 255 - 255 * CELLS[h][w]
            PIXELS[w, h] = (color, color, color)

    # Uncomment for saving the image
    # RESULT.save('RULE '+str(RULE_NUM))

    # Shows the image
    RESULT.show()

if __name__ == '__main__':

    RULE_NUM = bin(int(input('Rule\n')))[2:]
    RULE = format_ruleset(RULE_NUM)

    for time in range(16):
        CELLS.append(new_generation(CELLS,RULE,time))

    generate_image(CELLS)
