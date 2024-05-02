from mongoengine import connect
from faker import Faker
from random import randint, choice

from models import Student, Discipline

URI = "mongodb+srv://krom4rd:t6abZEUNgL1uhHVu@oleg.qq4u8pu.mongodb.net/?retryWrites=true&w=majority&appName=Oleg"

fake = Faker()
group_list = [
    'B11',
    'B12',
    'B13',
    'B14'
]


connect(host=URI, db='db')

student = Student(name=fake.first_name(),age=str(randint(18,30)),group=choice(group_list),discipline=[Discipline(discipline_name='History',discipline_teacher=fake.name())]).save()