from django.shortcuts import render,redirect
import sqlite3
from signup.models import UserDetails
# Create your views here.

def admin(request):
    print("----- In admin.admin ------")
    
    if request.method=='POST':
        data=request.POST
        username=data['username']
        password=data['password']
        u = next((u for u in UserDetails.objects.filter(uname=username)),None)
        print(u)
        print ("-------- ")
        
        #        return render(request, "wrongpassword.html")
        
        if u.uname!= 'admin':
            print("No such user")
            return render(request, "NoAccessPage.html")
        elif u.pswd != password:
            return render(request, "wrongpassword.html")
        
        return render(request, "adminpage.html")
    
    else:
        return render(request,"mainlogin.html")

def main(request):
    return render(request,'mainlogin.html')

#def adminPage(request):
    #return render(request,'adminpage.html')


# Create your views here.
