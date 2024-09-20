from django.shortcuts import render,redirect
from home.models import homepage,thomepage,studetails
# Create your views here.
def Shome(request):
    data=homepage.objects.all()
    homepagings={
        'data':data
    }
    return render(request,'shome.html',context=homepagings)

def Thome(request):
    data=homepage.objects.all()
    thomepagings={
        'data':data
    }
    return render(request,'thome.html',context=thomepagings)


def Home(request):
    data=homepage.objects.all()
    homepaging={
        'data':data
    }
    return render(request,'home.html',context=homepaging)
    
def Login(request):
    if request.method=='POST':
        suser=request.POST['username']
        spassword=request.POST['password']
        signin=homepage(username=suser,password=spassword)
        signin.save()
    return render(request,('login.html'))

def Tlogin(request):
    if request.method=='POST':
        tuser=request.POST['username']
        tpwd=request.POST['password']
        signin=thomepage(username=tuser,password=tpwd)
        signin.save()
    return render(request,('tlogin.html'))

def Signup(request):
    if request.method == 'POST':
        sname = request.POST['name']
        scourse = request.POST['course']
        htno = request.POST['hallticketno']
        semail = request.POST['email']
        spwd = request.POST['password']
        smob = request.POST['mobile']
        
        newss = homepage(name=sname,course=scourse,hallticketno=htno,email=semail,password=spwd,mobile=smob)
        newss.save()
        return redirect('/login')
    return render(request,'signup.html')

def Tsignup(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        mail = request.POST['email']
        pwd = request.POST['password']
        mob = request.POST['mobile']
        
        newts = thomepage(firstname=fname,lastname=lname,email=mail,password=pwd,mobile=mob)
        newts.save()
        return redirect('/tlogin')
    return render(request,'tsignup.html')


#def Viewgrades(request):
 #   return render(request,'view_grades.html')
 
def Studentdetails(request):
    if request.method == 'POST':
        sname = request.POST['studentname']
        shtno = request.POST['studenthallticketno']
        mlmark = request.POST['mlmarks']
        iotmark = request.POST['iotmarks']
        webmark = request.POST['webmarks']
        cnsmark = request.POST['cnsmarks']
        spmmark = request.POST['spmmarks']
        
        newsd = studetails(studentname=sname,studenthallticketno=shtno,mlmarks=mlmark,iotmarks=iotmark,webmarks=webmark,cnsmarks=cnsmark,spmmarks=spmmark)
        newsd.save()
    
    return render(request,'studetails.html')

def Studentdetailsdisplay(request):
    data=studetails.objects.all()
    return render(request,'studetailsdisplay.html',{'data':data})


def calculatetotal(request):
    stutotal=studetails.objects.all()
    totalmarks=studetails.totalmarks()
    return render(request,'studetailsdisplay',{'studetails':studetails,'totalmarks':totalmarks})

def calculategrade(request):
    stugrade=studetails.objects.all()
    grade=studetails.grade()
    return render(request,'studetailsdisplay',{'studetails':studetails,'grade':grade})

    