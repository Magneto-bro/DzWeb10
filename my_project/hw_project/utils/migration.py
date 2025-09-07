import sys
from pathlib import Path
import os
import django
from pymongo import MongoClient

BASE_DIR = Path(__file__).resolve().parent.parent / "my_project"
sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Author ,Quote ,Tag

client = MongoClient('mongodb://localhost:27017/')
db = client.hw

authors_cursor = db.authors.find()

for author in authors_cursor:
    Author.objects.get_or_create(
        fullname=author.get('fullname'),
        born_data=author.get('born_date'),      
        born_location=author.get('born_location'),
        description=author.get('description')
    )

quotes = db.quotes.find()

for quote in quotes:
    tags =[]
    for tag in quote['tags']:
        t,*_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exist_quote =bool(len(Quote.objects.filter(quote=quote['quote'])))
    
    if not exist_quote:
        author = db.authors.find_one({'_id':quote['author']})
        a =Author.objects.get(fullname = author['fullname'])
        q= Quote.objects.create(
            quote=quote['quote'],
            author =a

        )        

        for tag in tags:
            q.tags.add(tag)
