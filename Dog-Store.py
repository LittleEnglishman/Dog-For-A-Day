from bottle import run, route, get, post, request, view, static_file
from itertools import count
from datetime import datetime, timedelta

# BUILD LOG
# Version 1.0, created the main python framework with class and test dicitonary.
# Version 1.1, added in code for custom CSS and for Images
# Version 2.0, added in ability to use images/css files. Created the showcase page
# Version 3.0, made the personal dogs pages
# Version 3.1, added in rent functionality
# Version 4.0 , made the add a new dog function/the success page.




# Ver1.0 Class Dog creation
class Dog: 
    # Give each Dog object a key number
    _ids = count(0)
    
    # Set up initialised variable
    def __init__(self, name, age, gender, breed, friendliness, available, image):
        
        #Add new ID to dog
        self.id = next(self._ids)
        
        # Date to be added later
        self.date = None
        
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.friendliness = friendliness
        self.available = available
        self.image = image
        

# Ver1.0 data dictionary
dog_list = [
    Dog("Bruce", 5, "Male", "Bulldog", 3, 1, "/dog_image/Bruce.jpg"),
    Dog("Moses", 12, "Undecided", "Pussy Cat", 5, 1, "/dog_image/Moses.jpg"),
    Dog("Rex", 3, "Female", "Alpaca", 1, 0, "/dog_image/Rex.jpg"),
    Dog("Max", 4, "Male", "Bulldog", 3, 0, "/dog_image/Max.jpg"),
    Dog("Zula", 6, "Male", "Border Collie", 5, 1, "/dog_image/Zula.png")
    ]

# ver 6.0 
class Person:
    # Give each Person object a key number
    _ids = count(0)    
    
    def __init__(self, name, email):
        # Add new ID to person
        self.id = next(self._ids)
        
        self.name = name
        self.email = email
        
        # The dog will be added later
        self.dog = None
        
        
        
# Ver 6.0 data dictionary of persons
person_list = [
    Person("Moses", "Moses@gmail.com"),
    Person("Tom", "Tom@gmail.com"),
    Person("Jeremy", "Jeremy@gmail.com")
    ]

# Images Ver1.1
@route('/image/<filename>')
def server_static(filename):
    return static_file(filename, root='./Assets/Images')

# Dog Images Ver2.0
@route('/dog_image/<filename>')
def server_static(filename):
    return static_file(filename, root='./Assets/Images/Dogs')

# Code to be able to link custom css Ver1.1
@route('/<filename>.css')
def stylesheets(filename):
    return static_file('{}.css'.format(filename), root='./Assets')


# Ver1.0 Index page setup
@route('/')
@view('index')
def index():
    # Pass as no information needed for page
    pass


# Ver 2.0 Showcase-page
@route('/showcase-page')
@view('showcase-page')
def showcase_page():
    # Set dog_list to the data variable and return that to the page
    data = dict(dogs = dog_list)
    return data

# Ver 3.0 Personal Dog Pages
@route('/dog-page/<dog_id>')
@view('dog-page')
def dog_page(dog_id):
    # Set dog_id to integer
    dog_id = int(dog_id)
    found_dog = None
    
    # Loop through dog list to find the target dog
    for dog in dog_list:
        if dog.id == dog_id:
            found_dog = dog
            break
    #Return dogs data to page in form of a dictionary
    data = dict(dog = found_dog)
    return data

# Ver3.1 Rent a dog success
@route('/dog-rent-success/<dog_id>')
@view('dog-rent-success')
def dog_rent_success(dog_id): 
    """
    # Ver 6.0 Code added for human form
    name = request.forms.get("person-name")
    email = request.forms.get("email") 
    new_person = Person(name, email)
    new_person.dog = dog_id
    
    human_data = dict(human = new_person)
    
    person_list.append(new_person)
"""
    
    
    
    # Set dog_id to integer
    dog_id = int(dog_id)
    found_dog = None
    date = None

    # Loop through dog list to find the target dog
    for dog in dog_list:
        if dog.id == dog_id:
            found_dog = dog
            break
    # Return dogs data to page in form of a dictionary
    data = dict(dog = found_dog)
    found_dog.available = 0
    
    #Set new available date for the dog to be rented out + 1 day from today
    date = datetime.now() + timedelta(days=1)
    found_dog.date = date.strftime("%m/%d/%Y")  #datetime.now() + timedelta(days=1)
    
    # Return the created data to the page
    return data 
    
# Ver 4.0 Creating the new Dog page
@route('/new-dog')
@view('new-dog')
def new_dog():
    # Set dog_list to the data variable and return that to the page
    data = dict(dogs = dog_list)
    return data    

# New dog page action
@route('/new-dog-action', method="POST")
@view('new-dog-action')
def new_dog_action():
    name = request.forms.get("name")
    age = request.forms.get("age")
    gender = request.forms.get("gender")
    breed = request.forms.get("breed")
    friendliness = int(request.forms.get("friendliness"))
    
    # Create new Dog object (using placeholder image for now)
    new_dog = Dog(name,age,gender,breed,friendliness, 1, "/dog_image/Bruce.jpg")
    
    # Add new dog to the list oof
    dog_list.append(new_dog)
    
    # Return data in the form of a dictionary
    data = dict(dog = new_dog)
    return data    
    
    
    
    
    
# Bottle run 
run(host ='localhost', port = 8080, debug = True)


        