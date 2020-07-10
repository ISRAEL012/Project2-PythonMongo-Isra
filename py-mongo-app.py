import pymongo

db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(db_url)

database = client["PyDB_Local"] 
collection = database["employees"] 

def display_options():
    print("")
    print("1. Add a record")
    print("2. View a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Display records")
    print("6. Exit")
    user_option = input("Enter option number: ")
    return user_option

def get_record():
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    try:
        documnet=collection.find_one({'first_name':first.capitalize(), 'last_name':last.capitalize()})
    except:
        print("Error accessing the database")
    
    if not documnet:
        print("")
        print("Error! No results found.")
   
    return documnet 

# Our first function for CRUD:

def add_record(): 
    print("") 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    email = input("Enter the email: ")
    job = input("Enter the job title: ")
    hire = input("Enter the hire date: ")
    salary = float(input("Enter the salary: "))
    
    new_doc = { 
        "first_name": first.capitalize(),
        "last_name": last.capitalize(),
        "email": email.lower(),
        "job_title": job.capitalize(),
        "hire_date": hire,
        "salary": salary
    }

    try:
        collection.insert_one(new_doc)
        print("")
        print("Document inserted")
        print('=================')
    
    except:
        print("Error accessing the database")

def view_record():
    doc = get_record()
    if doc:
        print('View record')
        print('===========')   
        # if we do have some results we will continue with printing the full record
        for key, value in doc.items():
            if key!="_id":
                if (isinstance(value,str)):
                    print(key.capitalize(),": ", value.capitalize())
                     
                else:
                      print(key.capitalize(),": ", value)
                                        
def delete_record():
    doc = get_record() # getting the result from get_record() function

    if doc: # check if any result has been returned from get_record()
        print("")
        for key, value in doc.items():
            if key!="_id":
                if (isinstance(value,str)):
                    print(key.capitalize(),": ", value.capitalize())    
                else:
                      print(key.capitalize(),": ", value)  

        print("")
        confirm = input("Is this the document you want to delete?\nY or N: ")
        print("")

        # Our if condition to perform the delete operation or just ignore it based on the user's input
        if confirm.capitalize()=='y':
            try:
                collection.delete_one(doc)
                print("")
                print("Document deleted")
                print('================')
    
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")

def edit_record():
    
    doc = get_record()
    if doc: 
        update_doc = {} 
        print("") 
        for key, value in doc.items():
            if key != "_id":    
                
                if key == "salary":
                    
                    update_doc[key] = input(f"{key} [{value}]: ")
                    if (update_doc[key].isnumeric()):
                        update_doc[key] = float(update_doc[key])
                    else: 
                       update_doc[key] = value                   
                else:                    
                    update_doc[key] = input(f"{key} [{value}]: ").lower()
                
                if  update_doc[key]=="":
                    
                    update_doc[key] = value

        # for testing we will print the udpate_doc that contains all the values:
        print("") # Just printing a blank line
        print ("The new updated document:")
        print ("=========================")
        for key, value in update_doc.items():
            print(key,": [",value,"]")

        try:
            # we're going to call the collection.update_one() method: 
            collection.update_one(doc, { '$set': update_doc})     
            
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")
        
def display_records():
    print("")
    
    employees = collection.find({})
    for employee in employees:
        print(employee)            
        
def keep_asking():   
    while True: # It will be always true to keep running the while loop:        
        option = display_options()
            # here is the line for activating/calling our our function show_menu()
        if option == "1":
            # You will print a nice short message to confirm the user selected option
            print("You have selected option 1 for adding a new record")
            print("==================================================")
            # Then call a function to add a new record to the database
            add_record()
        elif option == "2":
            print("You have selected option 2 for viewing a record")
            print("===============================================")
            view_record() 
        elif option == "3":
            print("You have selected option 3 for modifying a record")
            print("=================================================")            
            edit_record()
        elif option == "4":
            print("You have selected option 4 for deleting a record")
            print("================================================")
            delete_record()
        elif option == "5":
            print("You have selected option 5 for display employees")
            print("================================================")
            display_records()    
        elif option == "6":
            # We should close our connection with MongoDB first:
            client.close()
            # Then we can exit the while loop and the entire application
       
            break
        else:
            print("Invalid Option!")


keep_asking()
