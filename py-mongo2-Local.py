import pymongo


db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(db_url)


database = client["PyDB_Local"] 
collection = database["employees"] 

employees = collection.find({}) 

#These comments below are to show us, our collection before to insert some new employees  
#for employee in employees:
  #  print(employee)

#firstly we must create a new variable and it can take any name
new_doc = { "first_name": "Kate", "last_name": "Willson", "email": "kate@gmail.com", "job_title": "designer", "hire_date": "2000-06-28", "salary": 27000.68 }

# We use insert_one or insert_many instead.
# collection.insert_one(new_doc)
collection.insert_one(new_doc)
employees = collection.find({})
for employee in employees:
    print(employee)


new_docs = [
{
 "first_name":"Alexa", "last_name": "Chow", "email": "alex@gmail.com", "job_title": "dba", "hire_date": "1999-10-30", "salary": 21006.09
},
{
 "first_name": "George", "last_name": "Martin", "email": "george@gmail.com", "job_title": "programmer", "hire_date": "2024-04-25", "salary": 19035.56
},
{
 "first_name":"Sarah", "last_name": "Grayson", "email": "sarah@gmail.com", "job_title": "professor", "hire_date": "2008-07-23", "salary": 24476.54
}
]

#This code is just to insert many elements
collection.insert_many(new_docs)

employees = collection.find({})
for employee in employees:
    print(employee)



