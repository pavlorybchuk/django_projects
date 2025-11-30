from django.db import models as m
from datetime import datetime

# Create your models here.
class Author(m.Model):
    first_name = m.CharField(max_length=50)
    last_name = m.CharField(max_length=50)

class Book(m.Model):
    title = m.CharField(max_length=50)
    publishing_year = m.IntegerField(default=datetime.now().year)
    price = m.DecimalField(max_digits=10, decimal_places=2)
    author = m.ForeignKey(Author, on_delete=m.CASCADE)
