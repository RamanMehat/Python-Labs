from Cimpl import *

def negative(img):
    """Modify the photo bound to img red, green, and blue components of each pixel to the opposite of their value"""  
    for pixel in img:
        x, y, col = pixel 
        r, g, b = col
        new_color = create_color(255 - r, 255 - g, 255 - b)
        set_color(img, x, y, new_color)
        
def grayscale(img):
    """Modify the photo bount to img to change each pixel's colours to an equivalent shade of grey"""
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        r = (r + g + b)/3
        r = g = b
        
        new_color = create_color(r, g, b)
        set_color(img, x, y, new_color)
        
def solarize(img, threshold):

    """
    Solarize the specified image.
    """
    
    for x, y, col in img:

        # Invert the values of all RGB components less than 128,
        # leaving components with higher values unchanged.

        red, green, blue = col

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)    
        
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
        
        else: # brightness is between 128 and 255, inclusive
            set_color(img, x, y, white)
            
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

        else: # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

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
            
def sepia_tint(img):
    grayscale(img)
    
    for x,y,col in img:
            red, green, blue = col
            dark_gray = create_color(red*1.1,green,blue*0.9)
            light_gray = create_color(red* 1.08,green,blue*0.93)
            medium_gray = create_color(red*1.15,green,blue*0.85)        
            
            if red < 63:
                set_color(img,x,y,dark_gray)
            elif red > 63 and red < 191:
                set_color(img,x,y,medium_gray)
            else:
                set_color(img,x,y,light_gray)
                
                
    def adjust_component(amount):
        if amount < 0:
            return 0
        elif amount < 63:
            return 31
        
        if amount > 64 and amount < 127 :
            return 95
        if amount > 128 and amount < 191:
            return 159
        else:
            return 223
    
        
    def posterize(img):
        for pixel in img:
            x, y, col = pixel
            red, green, blue = col    
            red = adjust_component(red)
        
            green = adjust_component(green)
            blue = adjust_component(blue)
            col = create_color(red,green,blue)
            set_color(img,x,y,col)
                
    def simplify(img):
        for x, y, col in img:
            red, green, blue = col    
            white = create_color(255,255,255)
            black = create_color(0,0,0)
            rgb1 = create_color(255,0,0)
            rgb2 = create_color(0,255,0)
            rgb3 = create_color(0,0,255)
            
            
            if red > 200 and green > 200 and blue > 200:
                set_color(img,x,y,white)
                
            if red < 50 and green < 50 and blue < 50:
                set_color(img,x,y,black)
                
            if red > green and red > blue:
                set_color(img, x, y, rgb1)
                
            if green > red and green > blue:
                set_color(img,x,y,rgb2)
            
            elif blue> red and blue > green:
                set_color(img,x,y,rgb3)
                
                
            
                
    