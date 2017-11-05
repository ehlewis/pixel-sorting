import csv, os
import bpy
from random import randint
from mathutils import Vector

array = []
importedArray = []
with open('/Users/evano/Documents/GitHub/pixel-sorting/picgreygrey.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            array.append(cleanedLine)
for i in range(0, len(array)):
    temp = []
    x = array[i]
    importedArray.append(list(map(int, x.split())))

# https://blender.stackexchange.com/questions/7358/python-performance-with-blender-operators
# https://blenderartists.org/forum/showthread.php?286325-Python-slowing-down-over-time

    #bpy.context.active_object.dimensions[2] = z #This works but I have literally no clue why this works but it doesnt with x or y
bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
ob = bpy.context.object
obs = []
sce = bpy.context.scene

for i in range(0,len(importedArray)-1):
    copy = ob.copy()
    copy.scale=((.5,.5,importedArray[i][2]))
    copy.location += Vector((importedArray[i][0], importedArray[i][1], 0))
    print("cell " + str(i) + " out of " + str(len(importedArray)))
    copy.data = copy.data.copy() # also duplicate mesh, remove for linked duplicate
    obs.append(copy)

for ob in obs:
    sce.objects.link(ob)

sce.update() # don't place this in either of the above loops!
