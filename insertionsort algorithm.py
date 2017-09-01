Example – looking at the insertionsort algorithm:

def jumbledlist ( maximumnumber, sizeoflist):  # here is the jumbledlist function
    import random
    jumbledlist = random.sample(range ( maximumnumber ), sizeoflist)
    return jumbledlist


A = jumbledlist(10 , 10) # a jumbled list sorted using built in methods.
print A
A.sort ()
print A


def insertionsort(data): # here is a exmaple of the insertionsort algorithm
    firstUnsorted = 0
    while firstUnsorted < len(data) - 1:
        indexOfSmallest = firstUnsorted
        index = firstUnsorted + 1
        while index <= len(data) - 1:
            if data[index] < data[indexOfSmallest]:
                indexOfSmallest = index
            index += 1
        data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]
        firstUnsorted += 1
    return data


print insertionsort(jumbledlist(20, 20)) # insertionsort algorithm sorting the jumbledlist output.

