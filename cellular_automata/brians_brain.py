"""
Brian's Brain cellular automaton implemented in Python.
https://en.wikipedia.org/wiki/Brian%27s_Brain
"""
import doctest

from PIL import Image

# Define some initial configurations for Brian's Brain
INITIAL_PULSER_PATTERN = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 0, 0, 0],
]

def compute_next_generation(current_cells: list[list[int]]) -> list[list[int]]:
    """
    Generates the next generation for a given state of Brian's Brain.
    
    >>> initial_state = [[0, 1, 0], [0, 2, 0], [0, 1, 0]]
    >>> compute_next_generation(initial_state)
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    """
    next_state = []
    for row_index in range(len(current_cells)):
        next_row = []
        for col_index in range(len(current_cells[row_index])):
            live_neighbour_count = sum(
                current_cells[row][col] == 1
                for row in range(row_index-1, row_index+2)
                for col in range(col_index-1, col_index+2)
                if (0 <= row < len(current_cells) and
                    0 <= col < len(current_cells[row_index]) and
                    (row, col) != (row_index, col_index))
            )
            if current_cells[row_index][col_index] == 1:
                next_row.append(2)
            elif current_cells[row_index][col_index] == 2:
                next_row.append(0)
            elif live_neighbour_count == 2:
                next_row.append(1)
            else:
                next_row.append(0)
        next_state.append(next_row)
    return next_state

def generate_animation_frames(initial_cells: list[list[int]], number_of_frames: int) -> list[Image.Image]:
    """
    Generates a list of images of subsequent Brian's Brain states.

    >>> initial_pattern = [
    ...     [0, 0, 0, 0, 0],
    ...     [0, 1, 2, 1, 0],
    ...     [0, 0, 0, 0, 0]
    ... ]
    >>> len(generate_animation_frames(initial_pattern, 5))
    5
    """
    animation_frames = []
    for _ in range(number_of_frames):
        img_frame = Image.new("RGB", (len(initial_cells[0]), len(initial_cells)))
        frame_pixels = img_frame.load()
        for x_coord in range(len(initial_cells)):
            for y_coord in range(len(initial_cells[0])):
                cell_state = initial_cells[y_coord][x_coord]
                pixel_color = (255, 255, 255) if cell_state == 0 else (0, 0, 0) if cell_state == 1 else (128, 128, 128)
                frame_pixels[x_coord, y_coord] = pixel_color
        animation_frames.append(img_frame)
        initial_cells = compute_next_generation(initial_cells)
    return animation_frames

if __name__ == "__main__":
    doctest.testmod()
    animation_frames = generate_animation_frames(INITIAL_PULSER_PATTERN, 16)
    animation_frames[0].save("brians_brain.gif", save_all=True, append_images=animation_frames[1:])
