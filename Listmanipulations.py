# list slicing

mylist = [1,2,3,4,5,6]

print(mylist[3:6])


#list comprehensions

cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

even = [2*i for i in range(10**100)]
print(even)
