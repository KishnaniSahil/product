from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello world</h1>")
def about(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * from post where pid =3")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={'keyposts':posts}
    return render(request,'kite/home.html',context)  
def insert(request):
    return render(request,'kite/form.html')
def match(request):
     Name = request.POST['blogTitle']
     Summary = request.POST['content']
     cursor = connection.cursor()
     cursor.execute("INSERT INTO post (`Name`,`Summary`) VALUES ( %s, %s );", (Name, Summary))     
