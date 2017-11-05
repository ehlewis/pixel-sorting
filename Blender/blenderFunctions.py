from PIL import Image
import os, sys, math, random
from time import time
import sorting
import argparse
import csv



def get_pixel(image, i, j):
    # Inside image bounds?
	width, height = im.size
	if i > width or j > height:
		return None
    # Get Pixel
	pixel = image.getpixel((i, j))
	return pixel

def convert_to_greyscale(image):
	img = image.convert('L')
	return img

def convert_to_array(image):
	outarray = []
	out = ''
	greyImage = convert_to_greyscale(image)
	file = open((args.image[:-4] + "grey.csv"), 'a+')

	with file as f:
		writer = csv.writer((f), delimiter = ' ')
		for y in range (0, height): # For each row
			for x in range (0, width): # For each pixel in the row
				pixel = get_pixel(image, x, y)
				greyscale = get_pixel(greyImage, x, y)
				writer.writerow([x, y, greyscale, pixel[0], pixel[1], pixel[2]])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process pictures and sort the pixels')
	parser.add_argument('image', metavar='image', type=str, help='the image to manipulate')
	parser.add_argument("-sort", help = "")
	args = parser.parse_args()

	try:
		im = Image.open(args.image)
		width, height = im.size
		print(args.image)
	except:
		sys.exit("ERROR: Image could not be found")

	elif args.sort == "greyscale": # This works well
		print "Converting to greyscale"
		img = convert_to_greyscale(im)
		img.save(args.image[:-4] + "grey.jpg")
		sys.exit('\x1b[1A' + '\x1b[2K' + "Converted to greyscale")
	elif args.sort == "array":
		convert_to_array(im)
		sys.exit("done")

	else:
		sys.exit("ERROR: Not an available method")
