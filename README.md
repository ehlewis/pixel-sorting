# pixel-sorting
### A visual take on sorting

This software will take an input image and line my line sort the pixels according to luminosity
Seeing as all the sort methods would yield the same result, there is a seeded option.
This seed will only sort a portion of the row, leaving more visual artifacts present in the final image

## Usage
`python pixelsmain.py -sort [bubblesort, selectionsortseed, bubblesortseed, quicksortseed] infile.jpeg`

## Examples

![alt text](https://github.com/ehlewis/pixel-sorting/blob/master/media/in.jpg?raw=true)

*Initial input*

![alt text](https://github.com/ehlewis/pixel-sorting/blob/master/media/bubblesort.jpg?raw=true)

*Bubble Sort*

![alt text](https://github.com/ehlewis/pixel-sorting/blob/master/media/bubblesortseed.jpg?raw=true)

*Bubble Sort Seeded*

## Unfinished work
There is a partial implementation to plug in with Blender
I'm unsure where I left off on this and it will likely be scrapped
