from PIL import Image
import os, sys, math, random
from time import time
import sorting
import argparse


def get_pixel(image, i, j):
    # Inside image bounds?
    if i > width or j > height:
      return None
    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

def lum (r,g,b):
 return math.sqrt( .241 * r + .691 * g + .068 * b )

def write_line(line):
    for x in range (0, width):
        value = (line[x][3], line[x][4], line[x][5])
        outMap[x,line[x][1]] = value

def parse():
	for y in range (0, height): # For each row
		lumrow = [] # Reset for each new row
		for x in range (0, width): # For each pixel in the row
			r, g, b = get_pixel(im, x, y)
			row.append([x, y, get_pixel(im, x, y), r, g, b]) # Stores the pixels in the order that we saw them
			lumrow.append([x, y, lum (r,g,b), r, g, b]) # Stores the pixels to be processed into luminosity order

		CURSOR_UP_ONE = '\x1b[1A'
		ERASE_LINE = '\x1b[2K'
		print(CURSOR_UP_ONE + ERASE_LINE + "Processing line " + str(y) + " of " + str(height))

		seed = random.randint(width/2,width)

		if args.sort == "selectionsortseed":
			sortedArray = sorting.selectionSortSEED(lumrow, seed)
		elif args.sort == "bubblesortseed":
			sortedArray = sorting.bubblesortSEED(lumrow, seed)
		elif args.sort == "bubblesort":
			sortedArray = sorting.bubblesort(lumrow)
		elif args.sort == "quicksortseed":
			sortedArray = sorting.lessthansoappend(sorting.quicksortSEED(lumrow, seed), row)

		write_line(sortedArray)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process pictures and sort the pixels')
	parser.add_argument('image', metavar='image', type=str, help='the image to manipulate')
	parser.add_argument("-sort", help = "Sorting algorithm ( )")
	args = parser.parse_args()

	if args.sort == "selectionsortseed":
	    print "Using Seeded Selection Sort"
	elif args.sort == "bubblesortseed": # This works better
	    print "Using Seeded Bubble Sort"
	elif args.sort == "bubblesort": # This works better
	    print "Using Bubble Sort"
	elif args.sort == "quicksortseed": # This works well
	    print "Using Seeded Quick Sort"
	else:
		sys.exit("ERROR: Not an available sorting method")

	try:
		im = Image.open(args.image)
		print(args.image)
	except:
		sys.exit("ERROR: Image could not be found")

	pixelMap = im.load()

	width, height = im.size
	row = []
	lumrow = []

	out = Image.new('RGB', (width, height))
	outMap = out.load()

	print(im.format, im.size, im.mode)
	print("Image width: " + str(width))
	print("Image height: " + str(height) + "\n\n")


	parse() # ALL THE WORK

	tm = str(time())
	outfile = args.image + tm[:-1] + ".jpg"

	try:
		out.save(outfile)
		print('\x1b[1A' + '\x1b[2K' + "Done! Saved as " + str(outfile))
	except:
		sys.exit("ERROR: Image could not be saved")
