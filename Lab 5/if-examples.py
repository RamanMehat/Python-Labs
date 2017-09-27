"""
SYSC 1005 Fall 2013
Image filters that use if/if-else/if-elif-else statements.
"""

from Cimpl import *

# if statement example

def solarize(img):
    """
    Solarize the specified image.
    """

    for x, y, col in img:

        # Invert the values of all RGB components less than 128,
        # leaving components with higher values unchanged.

        red, green, blue = col

        if red < 128:
            red = 255 - red

        if green < 128:
            green = 255 - green

        if blue < 128:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)

# if-else example

def black_and_white(img):
    """
    Convert the specified image to a black-and-white (two-tone) image.
    """

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on whether
    # its brightness is in the lower or upper half of this range.

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) / 3
        if brightness < 128:
            set_color(img, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(img, x, y, white)

# if-elif-else example

def black_and_white_and_gray(img):
    """
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, col in img:
        red, green, blue = col
        brightness = (red + green + blue) / 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

# Example: using boolean operators in an if statement's condition.

def swap_black_white(img):
    """
    Make all black pixels white and all white pixels black, leaving all
    other pixels unchanged.
    """

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        # Check if the pixel's colour is black; i.e., all three of its
        # components are 0.
        if red == 0 and green == 0 and blue == 0:

            # The pixel is black, make it white.
            set_color(img, x, y, white)

        # Check if the pixel's colour is white; i.e., all three of its
        # components are 255.
        elif red == 255 and green == 255 and blue == 255:

            # The pixel is white, make it black.
            set_color(img, x, y, black)


#-------------------------------------
# A few functions to test the filters.

def test_solarize():
    img = load_image("great_big_c.jpg")
    solarize(img)
    show(img)

def test_black_and_white():
    img = load_image("great_big_c.jpg")
    black_and_white(img)
    show(img)

def test_black_and_white_and_gray():
    img = load_image("great_big_c.jpg")
    black_and_white_and_gray(img)
    show(img)

def test_swap_black_white():
    img = load_image("checkerboard_bw.gif")
    show(img)
    swap_black_white(img)
    show(img)

    img = load_image("checkerboard_red_blue.gif")
    show(img)
    swap_black_white(img)
    show(img)

def test_all_filters():
    test_solarize()
    test_black_and_white()
    test_black_and_white_and_gray()
    test_swap_black_white()
