# List Manipulations

Garage = ["Ferrari", "Honda", "Porsche", "Toyota"]

def fetchlistrecord():
    for each_car in Garage:
	    print(each_car)

fetchlistrecord()
Garage[1] = "Maruti"

print(Garage)

# Tuple Manipulations

thistuple = ("Ferrari1", "Honda1", "Porsche1", "Toyota1")

def fetchtuplerecord():
    for each_car in Garage:
	    print(each_car)

fetchtuplerecord()
# thistuple[1] = "Maruti"
print(thistuple)

# Set Manipulations

thisset = {"apple", "banana", "cherry"}
#thisset[1] = "Mango"
print(thisset)

# Dictionary Manipulations

mydic = { 1:"test1", 2:"Test2"}
mydic[2] = "test23"
print(mydic)