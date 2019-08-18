def alogin(request):
    if request.method=="POST":
        username=data['username']
        password=data['password']
        conn=sqlite3.connect("db.sqlite3")
        cur=conn.cursor()
        cur.execute("select count(*) from Admin where username=?"(username,))
        result=cur.fetchall()
        x=result[0]
        if x[0]==1:
            cur.execute("select password from Admin where username=?"(username,))
            password1=cur.fetchall()
            if password==password1:
                return render(request,"#htmllink")
            else:
                print("wrong password")
                return redirect('mainlogin.html')
        else:
            print("username doesnt exist")
            return redirect('mainlogin.html')
    else:
        return render(request,"mainlogin.html")
        

\
  
