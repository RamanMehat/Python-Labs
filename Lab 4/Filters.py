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