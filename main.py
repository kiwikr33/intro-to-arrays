import array as arr 


a = arr.array('i', [1,2,3])

print("Original array:", a)


a.append(4)
print("After addding:", a)


a.remove(2)
print("After deleting:", a)