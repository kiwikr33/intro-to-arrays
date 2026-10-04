import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8,9])

largest = a[0]
second =a[1]

if second> largest:
    largest, second = second, largest

for i in range(2, len(a)):
    if a [i] > largest:
        second = largest
        largest = a[i]
    elif a[1] > second:
        second = a[i]

print("Second largest:", second)
