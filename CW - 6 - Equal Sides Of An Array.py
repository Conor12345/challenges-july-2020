def find_even_index(arr):
    if sum(arr[1:]) == 0:
        return 0
    for i in range(1, len(arr)):
        #print(arr[:i], arr[i], arr[i+1:])
        #print(sum(arr[:i]), sum(arr[i+1:]))
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))