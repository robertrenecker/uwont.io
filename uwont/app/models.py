from django.db import models
from mongoengine import *

class User(Document):
    firstname = StringField(max_length=200)
    lastname = StringField(max_length=200)
# Create your models here.
