from django.shortcuts import render,redirect
import sqlite3
from signup.models import UserDetails
# Create your views here.

def login(request):
	print("----- In login.login ------")

	if request.method=='POST':
		data=request.POST
		username=data['username']
		password=data['password']
		u = next((u for u in UserDetails.objects.filter(uname=username)),None)
		print(u)
		print ("-------- ")

#		return render(request, "wrongpassword.html")

		if u == None:
			print("No such user")
			return render(request, "wronguserid.html")
		elif u.pswd != password:
			return render(request, "wrongpassword.html")

		return render(request, "flightsearch.html")

	else:
		return render(request,"mainlogin.html")
		
def main(request):
	return render(request,'mainlogin.html')
		
def flightsearch(request):
	return render(request,'flightsearch.html')
        

