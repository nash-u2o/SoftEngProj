from django.shortcuts import render, redirect
from edu_app.models import User
import sqlite3

def index(request):
    context = { 

    }

    return render(request, 'index.html')

def home(request):
    print(request.session['student'])
    print(request.session['id'])
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def classpage(request):
    return render(request, 'classpage.html')
  
def login(request):
    #Add Later: If session id already assigned, automatically redirect. 
    #Logout option should redirect here and clear all session info
    
    if request.method == "POST":
        email = request.POST['user'] #Use email to log in
        password = request.POST['pass']

        #This would allow direct querying of the DB. Might allow SQL injection so avoid
        """ 
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor() #Cursor allows us to execute SQL statements and fetch results
        res = cur.execute("SELECT password FROM edu_app_user WHERE email=?", (email,))
        """

        res = User.objects.filter(email=email)
        if len(res) > 0:
            if res[0].password == password: #Successful login
                s_id =  res[0].id

                request.session['student'] = True
                request.session['id'] = s_id

                #Rendering doesn't perform desired functionality. Instead, we must redirect 
                return redirect('home')
            
            #Else some flag needs to be returned indicating invalid login
    
    return render(request, 'login.html')

def text(request):
    return render(request, 'text.html')
