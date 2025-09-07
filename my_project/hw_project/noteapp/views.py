from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.hw

def all_quotes(request):
    quotes = list(db.quotes.find())
    for q in quotes:
        author = db.authors.find_one({"_id": q["author"]})
        q["author_name"] = author["fullname"] if author else "Unknown"
    return render(request, "noteapp/all_quotes.html", {"quotes": quotes})

@login_required
def add_quote(request):
    authors = list(db.authors.find())
  
    authors_for_template = []
    for a in authors:
        authors_for_template.append({
            "id": str(a["_id"]),
            "fullname": a["fullname"]
        })
    
    if request.method =="POST":
        quote_text = request.POST.get("quote") 
        author_id = request.POST.get("author")

        db.quotes.insert_one({
            'quote':quote_text,
            'author':ObjectId(author_id),
            "created":datetime.datetime.now()
        })
        return redirect("quotes:all_quotes")  
    return render(request, "noteapp/add_quote.html", {"authors": authors_for_template})