from PIL import Image
import os, sys, math, random
from time import time
import sorting




im = Image.open("test.jpg")
pixelMap = im.load()

pixelMap = im.load()

width, height = im.size
row = []
lumrow = []
#sortedArray = []

out = Image.new('RGB', (width, height))
outMap = out.load()

print(im.format, im.size, im.mode)





def get_pixel(image, i, j):
    # Inside image bounds?
    #width, height = image.size
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


'''for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
'''


print(width)
print(height)

for y in range (0, height):
    lumrow = []
    for x in range (0, width):
        r, g, b = get_pixel(im, x, y)
        row.append([x, y, get_pixel(im, x, y), r, g, b])
        lumrow.append([x, y, lum (r,g,b), r, g, b])
    print(y)
    seed = random.randint(width/2,width)
    #sortedArrayTemp = sorting.quicksort(lumrow)
    #sortedArrayTemp = sorting.quicksortSEED(lumrow, random.randint(0,width))
    sortedArray = sorting.selectionSortSEED(lumrow, seed)
    #sortedArray = sorting.selectionSort(lumrow)
    #sortedArray = sorting.bubblesortSEED(lumrow, seed)

    #sortedArray = sorting.lessthansoappend(sorting.quicksortSEED(lumrow, seed), row)

    write_line(sortedArray)

t = time()
tm = str(t)


outfile = "outL" + tm[:-1] + ".jpg"
out.show()
out.save(outfile)
