# Looks too good
def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0][2]
        #print (str(pivot))

        n = 0
        while n < len(array):
            if array[n][2] < pivot:
                less.append(array[n])
            if array[n][2] == pivot:
                equal.append(array[n])
            if array[n][2] > pivot:
                greater.append(array[n])
            n += 1
        '''for i in array:
            if i < pivot:
                less.append(i)
            if i[2] == pivot:
                equal.append(i)
            if i[2] > pivot:
                greater.append(i)'''
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

# Def a bad idea but works with lessthansoappend only
def quicksortSEED(array, seed):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0][2]
        n = 0
        while n < seed and n < len(array):
            """print (str(pivot))
            print(array[n][2])"""
            if array[n][2] < pivot:
                less.append(array[n])
            if array[n][2] == pivot:
                equal.append(array[n])
            if array[n][2] > pivot:
                greater.append(array[n])
            n += 1

        # Don't forget to return something!
        return quicksortSEED(less, seed)+equal+quicksortSEED(greater, seed)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

# Slow AAAFFFFF but needed for seeded quick sort otherwise we get out of bound errors
def lessthansoappend(sorted, original):
    i = 0
    j = 0
    while i < len(sorted):
        while j < len(original):
            if(sorted[i][0] == original[j][0] and sorted[i][1] == original[j][1]):
                original.remove(original[j])
            j += 1
        i += 1
    difference = len(original) + 1 - len(sorted) + 1
    n = 0
    while n < difference:
        sorted.append(original[n])
        n += 1
    return sorted

def selectionSort(line):
   for fillslot in range(len(line)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if line[location][2]>line[positionOfMax][2]:
               positionOfMax = location

       temp = line[fillslot]
       line[fillslot] = line[positionOfMax]
       line[positionOfMax] = temp
   return line

def selectionSortSEED(line, seed):
    i = 0
    while i < seed and i < len(line): # range(len(line)-1,0,-1)
        positionOfMax=0
        for location in range(1,i+1):
            if line[location][2]>line[positionOfMax][2]:
                positionOfMax = location

        temp = line[i]
        line[i] = line[positionOfMax]
        line[positionOfMax] = temp
        i += 1
    return line

def bubblesort( line ):
	for i in range( len( line ) ):
		#for k in range( len( line ) - 1, i, -1 ):
		for k in range( len( line ) - 1, i, -1 ):
			if ( line[k][2] < line[k - 1][2] ):
				swap( line, k, k - 1 )
	return line

def bubblesortSEED( line, seed ):
    for i in range( len( line ) ):
        for k in range( 0, seed, 1 ):
            if ( line[k][2] < line[k - 1][2] ):
                swap( line, k, k - 1 )
    return line

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
