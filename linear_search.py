def linear_search(arr, arr_len, x):
    for i in range(0, arr_len):
        if arr[i] == x:
            return i
    return -1

# linear search test case
def linear_search_test(arrlist,xlist):
    #take a list of list and a list of value which need to find sent them through the linear search function using loop
    arr_list_len = len(arrlist)
    for i in range(0, arr_list_len):
        arr = arrlist[i] # parse single list from arrlist
        arr_len = len(arr)
        x = xlist[i]  # parse a single value from xlist that need to find
        result = linear_search(arr, arr_len, x)
        if result == -1:
            print("Element not found")
        else:
            print("Element found at index", result)

arrlist = [[1, 5, 7, 9, 10],[7, 56, 77, 99, 100],[11, 57, 87, 19, 98]]
xlist= [1, 3, 5]
linear_search_test(arrlist,xlist)