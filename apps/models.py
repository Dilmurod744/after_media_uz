from django.db import models
from django.db.models import Model, CharField, EmailField, TextField, FileField, ImageField


class User(Model):
    name = CharField(max_length=30)
    email = EmailField()
    phone = CharField(max_length=15)
    message = TextField()


class Video(Model):
    # name = CharField(max_length=25)
    video = FileField(upload_to='videos/')

    def __str__(self):
        return self.id


class Photo(Model):
    name = CharField(max_length=25)
    photo = ImageField(upload_to='images/')

    def __str__(self):
        return self.name
