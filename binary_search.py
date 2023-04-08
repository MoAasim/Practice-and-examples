

def binarySearch(list, num):
    start = 0
    end = len(list) - 1

    while (start <= end):
        mid = (start + end)//2
        if (list[mid] == num):
            return mid
        elif (list[mid] > num):
            end = mid - 1
        else:
            start = mid + 1
    
    return -1
          

myList = [9,4,2,6,5,7,8]

print("Unsorted list:\n", myList)
myList.sort()
print("Sorted list:\n", myList)

num = int(input("Enter num to serach:"))

numFound = binarySearch(myList, num)

if numFound != -1:
    print("Num is found at index:", numFound)
else:
    print("Num is not present in the list")