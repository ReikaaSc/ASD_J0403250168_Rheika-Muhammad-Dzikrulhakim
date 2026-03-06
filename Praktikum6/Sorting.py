def bubblesort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                # tukar dua data yang salah urutannya
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                
data = [54,26,93,17,77,31,44,55,20]
bubblesort(data)
print(data)

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
        
alist=[70, 30, 100, 20, 60, 110, 40, 80, 50, 90]
shortBubbleSort(alist)
print(alist)

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if data[location] > data[positionOfMax]:
                positionOfMax = location
        
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp
    
data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)

def insertionSort(data):
    for index in range(1,len(data)):
        
        currentvalue = data[index]
        position = index
        
        while position > 0 and data[position- 1] > currentvalue:
            data[position] = data[position - 1]
            position = position - 1
            
        data[position] = currentvalue
        
data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)

def shellSort(data):
    sublistcount = len(data)//2
    while sublistcount > 0:
        
        for startposition in range(sublistcount):
            gapInsertionSort(data,startposition,sublistcount)
            
        print("After increments of size",sublistcount,"The list is",data)
        
        sublistcount = sublistcount // 2

def gapInsertionSort(data,start,gap):
    for i in range(start+gap,len(data),gap):
        
        currentvalue = data[i]
        position  = i
        while position >= gap and data[position-gap] > currentvalue:
            data[position] = data[position-gap]
            position = position - gap
            
        data[position] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
shellSort(data)
print(data)

def mergeSort(data):
    print("Splitting ",data)
    if len(data)>1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1
            
        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1
            
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1
            
        print("Merging ",data)
        
data = [54,26,93,17,77,31,44,55,20]
mergeSort(data)
print(data)

def quickSort(data):
    quickSortHelper(data,0,len(data)-1)
    
def quickSortHelper(data,first,last):
    if first<last:
        splitpoint = partition(data,first,last)
        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)
        
def partition(data,first,last):
    pivotvalue = data[first]
    
    leftmark = first+1
    rightmark = last
    
    done = False
    while not done:
        
        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            
        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
            
        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
            
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    
    return rightmark

data = [54,26,93,17,77,31,44,55,20]
quickSort(data)
print(data)