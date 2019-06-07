from bottle import run, route, get, post, request, view, static_file
from itertools import count
from datetime import datetime, timedelta
"""
# BUILD LOG
# Version 1.0, created the main python framework with class and test dicitonary.
# Version 1.1, added in code for custom CSS and for Images
# Version 2.0, added in ability to use images/css files. Created the showcase page
# Version 3.0, made the personal dogs pages
# Version 3.1, added in rent functionality
# Version 4.0 , made the add a new dog function/the success page.



# Version 8.0, made the new function for the admin page
"""


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
        
        # These will be added later
        self.dog = None
        self.dog_name = None
        self.return_date = "0/0/0"
        
        
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
@route('/dog-rent-success/<dog_id>', method = "POST")
@view('dog-rent-success')
def dog_rent_success(dog_id): 

    # Ver 6.0 Code added for human form
    # Set the variables
    name = request.forms.get("person-name")
    email = request.forms.get("email") 
    new_person = Person(name, email)
    new_person.dog = dog_id
    
    
    # Find the dog being rented
    dog_id = int(dog_id)
    found_dog = None
    for dog in dog_list:
        if dog.id == dog_id:
            found_dog = dog
            break    
    # Set dogs availablity to 0 (unavailable)
    found_dog.available = 0
    # Add dogs name to the person
    new_person.dog_name = found_dog.name
    
    
    #Set new available date for the dog to be rented out + 1 day from today
    date = datetime.now() + timedelta(days=1)
    
    #Set the date on both the dog and person object
    dog.date = date.strftime("%d/%m/%Y") 
    new_person.return_date = date.strftime("%d/%m/%Y")  #datetime.now() + timedelta(days=1)
    
    human_data = dict(human = new_person)
    
    person_list.append(new_person)    
    # Return the created data to the page
    return human_data
    
# Ver 4.0 Creating the new Dog page
@route('/new-dog')
@view('new-dog')
def new_dog():
    # Set dog_list to the data variable and return that to the page
    data = dict(dogs = dog_list)
    return data    

# Ver 4.0 New dog page action
@route('/new-dog-action', method="POST")
@view('new-dog-action')
def new_dog_action():
    
    # Get the variables form the form
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
    
# Ver 7.0 return page   
@route('/return-page')
@view('return-page')
def return_page():
    # Set dog_list to the data variable and return that to the page
    data = dict(dogs = dog_list)
    return data
# Ver 7.0
@route('/return-success/<dog_id>')
@view('return-success')
def return_success(dog_id):
    
    # Find the dog within the list
    dog_id = int(dog_id)
    found_dog = None
    for dog in dog_list:
        if dog.id == dog_id:
            found_dog = dog
            break    
    # Set availablity to 1
    data = dict(dog = found_dog)
    found_dog.available = 1
    
    
    # Find the owner of the current dog
    found_person = None
    for person in person_list:
        if person.dog_name == dog.name:
            found_person = person
            break
    # Remove dog name from person class only if it doesn't have one to begin with
    if found_person.dog_name != None:
        found_person.dog_name = None
        
    return data  

# Ver 8.0 Admin Page
@route("/admin-page")
@view("admin-page")
def admin_page():
    # Set person_list to the data variable and return that to the page
    data = dict(humans = person_list)
    return data      
    
# Bottle run 
run(host ='localhost', port = 8080, debug = True)


        