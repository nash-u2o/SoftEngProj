from django.shortcuts import render
import sqlite3

def index(request):
    context = { 

    }

    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor() #Cursor allows us to execute SQL statements and fetch results
        email = request.POST['user'] #Use email to log in
        password = request.POST['pass']
        res = cur.execute(f"SELECT password FROM edu_app_user WHERE email=?", (email,))
        if res.fetchone()[0] == password:
            return render(request, 'home.html')

    return render(request, 'login.html')
