# SYSC 1005 A Fall 2013 Lab 7
# Revised: October 22, 2013.

import sys  # get_image calls exit
#from Cimpl import *
from Filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img



if __name__ == "__main__":
    
    Finished = False
    image_loaded = False
    while not Finished:
    
	command = raw_input("Load Image, Negative Image, Grayscale, Posterize, Sepia Tint, Edge Detect, or Quit (L, N, G, P, S, E, Q): ")
	if command in ['L', 'N', 'G', 'P', 'S', 'E', 'Q']:
	    if command == 'L':
	        img = get_image()
	        image_loaded = True
	        show(img)  
	        
	    elif command == 'N' and image_loaded == True:
		#img = get_image()
		negative(img)
		show(img)
		
	    elif command == 'G' and image_loaded == True:
		#img = get_image()
		grayscale(img)
		show(img)
    
	    elif command == 'P' and image_loaded == True:
		#img = get_image()
		posterize(img)
		show(img)	
	    
	    elif command == 'S' and image_loaded == True:
		#img = get_image()
		sepia_tint(img)
		show(img)	
		
	    elif command == 'E' and image_loaded == True:
		#img = get_image()
		threshold = float(raw_input())
		detect_edges_better(img, threshold)
		show(img)
    
	    elif image_loaded == False:
	       
		print 'No Image Loaded'
		
	    elif command == 'Q': 
		Finished = True 
		
	else:
	    print command, 'No such command'