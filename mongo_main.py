from pymongo.mongo_client import MongoClient
from faker import Faker
from random import randint, choice

fake = Faker()

URI = "mongodb+srv://krom4rd:t6abZEUNgL1uhHVu@oleg.qq4u8pu.mongodb.net/?retryWrites=true&w=majority&appName=Oleg"

client = MongoClient(URI)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.db.university
# update = db.university.update_one({"name":"Oleh"},{"$set": {"group":"B11"}})

# update = db.university.update_one({"name":"Olena"},{"$set": {"group":"B11"}})


# student = db.university.find_one({"name" : "Oleh"})

# print(student)

# group = db.university.find({'group' : 'B11'})
# print(list(group))

def update_one(filter, filter_value, new_column, new_column_value):
    select_to_update = db.find_one({filter : filter_value})
    if select_to_update:
        db.update_one({filter : filter_value},{"$set" : {new_column : new_column_value}})
        print(f'Old values = {select_to_update}')
        print(f'Column: {new_column} update value to: {new_column_value} for {filter_value} secces')
        print(f'New values = {db.find_one({filter : filter_value})}')
    else:
        print(f"In db not find {filter} : {filter_value}")

def random_seeds(number:int):
    group_list = ['B11','B12','B13','B14']
    student_list = [{'name': fake.first_name(), 'age': randint(18,30), 'group': choice(group_list)} for _ in range(number)]
    db.insert_many(student_list)
    
def create_random_student_object():
    group_list = ['B11','B12','B13','B14']
    return {'name': fake.name(), 'age': randint(18,30), 'group': choice(group_list)}


def ready_column(column_name):
    full_db = db.find({})

    for student in full_db:
        if column_name in student:
            print(student)

if __name__=="__main__":
    random_seeds(2)
    