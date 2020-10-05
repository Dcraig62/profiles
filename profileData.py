class profile:
    def __init__(self, name, age, description):
        self.name = name 
        self.age = age
        self.description = description 

def getName():
    name = input("Enter a name: ")
    return name

def getAge():
    age = input("Enter your age: ")
    return age

def description():
    description = input("Describe yourself: ")
    return description

def addProfile(name):
    person = profile(name, getAge(), description())
    return person

def displayProfile(name, thisDict):
    if name in thisDict:
        x = thisDict.get(name)
        print("Name: " + str(x.name))
        print("Age: " + str(x.age))
        print(str(x.description))
    else:
        print("Error! Name not found")

def displayNames(thisDict):
    print("Names on files: ")
    for x in thisDict:
        n = thisDict[x]
        print(n.name)

example = profile("example", 0, "This is not a real person")
thisDict = {
    "example" : example
}
displayProfile("example", thisDict)
x = 's'
while x != 'Q':
    print("Enter one of the following: ")
    print("A - to add a profile")
    print("D - to display a profile")
    print("N - to print all the names")
    print("Q - to quit")
    print()
    x = input("Enter a letter: ")
    if x == 'A' or x == 'D':
        name = getName()
        if x == 'A':
            person = addProfile(name)
            thisDict[name] = person
        else:
            displayProfile(name, thisDict)
    elif x == 'N':
        displayNames(thisDict)
    elif x != 'Q':
        print("Not a valid option!")
    

