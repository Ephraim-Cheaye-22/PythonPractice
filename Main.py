def topFiveMovies():
    #Print the first movie
    print("Into the Spider Verse")

    #Print second movie
    print("The Dark Knight")

    #Print third movie
    print("The Black Pearl")

    #Print fourth movie
    print("Black Panther")

    #Print fifth movie
    print("A Silent Voice")

print("these are my top five movies")
topFiveMovies()

def favoriteFastFoodPlaces():
    #Print the First Place
    print("Five Guys")

    #Print the Second Place
    print("Dairy Queen")

    #Print the Third Place
    print("Culvers")

    #Print the Fourth Place
    print("Subway")

    #Print the Fifth Place
    print("Wendys")

print("these are my favorite Fast Food Places")
favoriteFastFoodPlaces()

#define a Function that outputs your name
#followed by "is my name"
def myNameIs(turtle):

    #output string
    print(turtle + "is my name")

#run function
myNameIs("Ephraim")

def timesTwo(x):
    print(x * 2)

timesTwo(30)

def plusFive(x):
    print(x + 5)

plusFive(10)

def divideTwo(x):
    print(x / 2)

divideTwo(20)

def addTwoNumbers(x, y):
    print(x + y)

addTwoNumbers(10,59)

def madLimb(a, b, c, d, e, f, g, h, i, j):
    print("Star wars is a" + a + b + "of" + c + "versus evil in a" + d + "far far away." "There are" + e + "battles between" + f + g + "in" + h + "space and" + i + "duels with" + j)

madLimb("Huge", "pool", "cold", "Beach", "Hairy", "Smelly", "Toyotas", "Chubby", "Cheeto", "Dark")

def greaterThan10(x):
    if x > 10:
        return "x is greater than 10"
        
    elif x == 10:
        return "x equals 10"
    else:
        return "x is not greater than 10"

print(greaterThan10(5))

def equalsTen(x):
    if x == 10:
        return "x equals 10!!!!!!"

    elif x > 10:
        return "x is greater than 10"

    else:
        return "x is not equal to 10"

print(equalsTen(10))

def favColor(color):
    if color == "red":
        return "your favorite color is red"
    else:
        return "your favorite color is not red"

print(favColor("red"))

def define(word):

    word = word.lower()
    
    if word == "simple":
        return "easily understood"
    elif word == "nice":
        return "pleasant"
    elif word == "brave":
        return "ready to face danger"
    elif word == "real":
        return "actually exists"
    elif word == "copy":
        return "a thing made to similar to another"
    elif word == "evil":
        return "profoundly wicked"
    elif word == "sin":
        return "immoral act"
    elif word == "hero":
        return "a person who is admired for their courage"
    elif word == "save":
        return "keep safe"
    elif word == "fun":
        return "enjoyment"
    else:
        return "definition not given"
print(define("fun"))

print(abs(5-7))

print(23 % 10)

print(5 % 2)

def evenOrOdd(x):
    if x % 2 == 0:
        return True
    else:
        return False


def twoBigNumbers(x, y):
    if x > 10 and y > 10:
        return True
    else:
        return False

def twoBigNumbers(x, y):
    if x > 10 or y > 10:
        return True
    else:
        return False

def twoBigNumbers(x, y):
    if x > 10 or not y > 10:
        return True
    else:
        return False

def function(x, y, z):
    if x > 10 or not y > 10 and z == 5:
        return True
    else:
        return False
        
def function():

    count = 5

    while count <= 100:
        print(count)
        count = count + 5


function()

def ha():

    count = 1

    while count <= 100:
        print(count)
        count =  count + 1
 
ha()

def ra():
    count = 1
    potato = 1

    while potato <= 10:
        while count <= 10:
            print(count)
            count = count + 1
        potato = potato + 1
        count = 1

ra()