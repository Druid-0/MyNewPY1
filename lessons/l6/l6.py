


array_1 = (1,2,3,4,5,6,7)

def find_item(array,target):

    for i in array:
        count = 0
        if target == i:
            i += count
            print(count, ' found')
        else:
            i += count
            print(count + i,"-", 'not found')

find_item(array_1, 5)


def binary_search(array, target):
    left, right = 0, len(array) -1

    while left <= right:
        mid = (left + right) // 2
