""" SYSC 1005 A Fall 2013 Lab 4
Image processing examples.

D.L.Bailey, SCE, Carleton University
"""

from Cimpl import *
from Filters import *

def maximize_red(img):
   """ Modify the photo bound to img to look like it was taken at 
   sunset, by maximizing the red component of every pixel.
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      new_color = create_color(255, g, b)
      set_color(img, x, y, new_color)

def make_sunset(img):
   """ Modify the photo bound to img to look like it was taken at 
   sunset, by reducing the green and blue components of every pixel.
   """
   for pixel in img:
      x, y, col = pixel  
      r, g, b = col

      g = g * 0.7 # decrease green by 30%
      b = b * 0.7 # decrease blue by 30%

      col = create_color(r, g, b)
      set_color(img, x, y, col)

def remove_blue(img):
   """ Modify the photo bound to img so all the blue is removed. """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      new_color = create_color(r, g, 0)
      set_color(img, x, y, new_color)
      
def half_colours(img):
   """Modify the photo bound to img so red, green, and blue pixels are all halfed."""
   for pixel in img:
      x, y, col = pixel 
      r, g, b = col
      
      r = r * 0.5 # decrease red by 50%
      g = g * 0.5 # decrease green by 50%
      b = b * 0.5 # decrease blue by 50%      
      
      col = create_color(r, g, b)
      set_color(img, x, y, col)      