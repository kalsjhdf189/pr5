import sqlite3

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    c = sqlite3.connect('cvetok.db')
    cur = c.cursor()
    cur.execute("SELECT Название,Цена FROM flowers")
    test = cur.fetchall()
    return render(request, 'index.html' , {'test': test})

def news(request):
    c = sqlite3.connect('cvetok.db')
    cur = c.cursor()
    cur.execute("SELECT Название,Описание,Дата FROM News")
    test = cur.fetchall()
    return render(request, 'news.html', {'test': test})

def review(request):
    return render(request, 'review.html')