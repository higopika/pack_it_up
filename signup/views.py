from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import UserDetails
import csv
import sqlite3

# Create your views here.
def sdetail(request):
	if request.method=='POST':
		print("----- In sdetail -------")
		data=request.POST
		username=data['username']
		first_name=data['first_name']
		last_name=data['last_name']
		email=data['email']
		password1=data['password1']
		password2=data['password2']
		
		if password1==password2:
			print("---- About to insert data ------")
			user = UserDetails(uname=username, fname=first_name, lname=last_name, email=email, pswd=password1)
			user.save()
		else:
			print("not matching")
			return render(request,'mainlogin.html')
		
		return render(request, "tnxsignup.html")
		
	else:
		return redirect('mainlogin.html')


def login(request):
	if request.method=='POST':
		data=request.POST
		name=data['sname']
		password1=data['spassword1']
		return render(request,'userpage.html')
  

def main(request):
	return render(request,'mainlogin.html')
        
def tnx(request):
	return render(request,'tnxsignup.html')

