from bottle import run, route, get, post, request, view, static_file
from itertools import count

# BUILD LOG
# Version 1.0, created the main python framework with class and test dicitonary.

# Ver1.0 Class Dog creation
class Dog: 
    # Give each Dog object a key number
    _ids = count(0)
    
    # Set up initialised variable
    def __init__(self, name, age, gender, breed, friendliness, available):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.friendliness = friendliness
        self.available = available

# Ver1.0 data dictionary
dog_list = [
    Dog("Bruce", 5, "Male", "Bulldog", 3, True),
    Dog("Moses", 12, "Female", "Pussy Cat", 5, True),
    Dog("Rex", 3, "Female", "Alpaca", 1, False),
    Dog("Max", 4, "Male", "Bulldog", 3, False),
    Dog("Zula", 6, "Male", "Border Collie", 5, True)
    ]

# Ver1.0 Index page setup
@route('/')
@view('index')
def index():
    # Pass as no information needed for page
    pass

#Bottle run 
run(host ='localhost', port = 8080, debug = True)


        