def bubble(list):
    for i in range(len(list) - 1):
        for sort in range(len(list) - 1):
            if list[sort] > list[sort + 1]:
                temp = list[sort]
                list[sort] = list[sort + 1]
                list[sort + 1] = temp
        sort = 0
    return list

def selection(list):
    #Iterate over the list
    for sorted in range(len(list)-1):
        minimum = sorted
        #find the smallest value in the unsorted portion of the list
        for check in range(sorted + 1, len(list)):
            if list[minimum] > list[check]:
                minimum = check

        #swap the smallest value found with the first unsorted value of the list
        temp = list[minimum]
        list[minimum] = list[sorted]
        list[sorted] = temp
    
    return list

def insertion(list):
    #iterate over the list started at the 2nd element
    for sorted in range(1, len(list)):
        check = sorted
        #Check to see if the element on front of the sorted list is less than the element at the end of the sorted list
        #Then insert that element into the correct spot in the list
        while (list[check] < list[check - 1]) and (check > 0):    
            #Swap the two elements if the rightmost one is smaller
            temp = list[check]
            list[check] = list[check - 1]
            list[check - 1] = temp
            check -= 1

    return list




def insertion2(list, gap, start):
    #iterate over the list
    for sorted in range(gap + start, len(list), gap):
        check = sorted
        #Check to see if the element on front of the sorted list is less than the element at the end of the sorted list
        #Then insert that element into the correct spot in the list
        while (check > 0) and (list[check] < list[check - gap]):    
            #Swap the two elements if the rightmost one is smaller
            temp = list[check]
            list[check] = list[check - gap]
            list[check - gap] = temp
            check -= gap

    return list

def shell(list):
    power = 0
    remainder = len(list)
    gapList = []
    #Find the nearest power of two below the list
    while (remainder > 1):
        remainder //= 2
        power += 1
        gapList.append((2 ** (power)) - 1)
    for x in range(len(gapList) - 1, -1, -1):
        start = 0
        while (((start + gapList[x]) < len(list)) and (start < gapList[x])):
            list = insertion2(list, gapList[x], start)
            start += 1

    return list




def partition(list, low, high):
    middle = (low + high)//2
    pivot = list[middle]
    while(True):
        while list[high] > pivot:
            high -= 1
        while list[low] < pivot:
            low += 1

        if low >= high:
            break

        else:
            #swap the numbers
            temp = list[low]
            list[low] = list[high]
            list[high] = temp

    return (high)
    

def quick(list, low, high):
    if low >= high:
        return
    splitting = partition(list, low, high)
    quick(list, low ,splitting - 1 )
    quick(list, splitting + 1, high)

    return list

def quicksort(list):
    quick(list, 0, len(list) - 1)

