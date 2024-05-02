from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField, DateTimeField

class Discipline(EmbeddedDocument):
    discipline_name = StringField(required=True)
    discipline_teacher = StringField(required=True)


class Student(Document):
    name = StringField()
    age = StringField()
    group = StringField()
    discipline = ListField(EmbeddedDocumentField(Discipline), required=True)