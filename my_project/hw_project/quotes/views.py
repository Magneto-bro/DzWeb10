from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

from .utils import get_mongdb


def main(request, page=1):
    db = get_mongdb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_in_page = paginator.page(page)
    return render(request , 'quotes/index.html',context={'quotes':quotes_in_page})