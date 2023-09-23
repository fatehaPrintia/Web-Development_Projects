from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from home.models import add_resources,faculty
from home.models import faculty
from home.forms import UploadFileFrom
from home.forms import Facultyinfo

# Create your views here.
@login_required(login_url='login')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
def registration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('mail')
        if "@g.bracu.ac.bd" not in email:
            return HttpResponse("Enter Valid BracU g-suit !!!!")
        
        if len(uname)!=8:
             return HttpResponse("Enter Valid BracU Student Id!!!!")
        if uname[:1]>'23' or uname[2] not in '123' or uname[3:5] not in ['01','04'] :
            return HttpResponse("Enter Valid BracU Student Id!!")
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'registration.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/Home")

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def CourseInformation(request):
    return render (request,'courseinfo.html')
def Courses(request):
    return render (request,'courses.html')
def cse1(request):
    course_list = add_resources.objects.filter(Course__icontains='cse1')
    
    c = {}
    for i in course_list:
        if i.Course in c:
            c[i.Course]+=[i]
        else:
            c[i.Course]=[i]
    print(c)
    context={
        'data':c
    }
    return render (request,'cse1.html',context)
def cse2(request):
    
    course_list = add_resources.objects.filter(Course__icontains='cse2')
    
    c = {}
    for i in course_list:
        if i.Course in c:
            c[i.Course]+=[i]
        else:
            c[i.Course]=[i]
    print(c)
    context={
        'data':c
    }
    return render (request,'cse2.html',context)
def cse3(request):
    course_list = add_resources.objects.filter(Course__icontains='cse3')
    
    c = {}
    for i in course_list:
        if i.Course in c:
            c[i.Course]+=[i]
        else:
            c[i.Course]=[i]
    print(c)
    context={
        'data':c
    }
    return render (request,'cse3.html',context)

def cse4(request):
    
    course_list = add_resources.objects.filter(Course__icontains='cse4')
    
    c = {}
    for i in course_list:
        if i.Course in c:
            c[i.Course]+=[i]
        else:
            c[i.Course]=[i]
    print(c)
    context={
        'data':c
    }
    return render (request,'cse4.html',context)

def mns1(request):
    
    course_list = add_resources.objects.filter(Course__icontains='mat1')
    
    c = {}
    for i in course_list:
        if i.Course in c:
            c[i.Course]+=[i]
        else:
            c[i.Course]=[i]
    print(c)
    context={
        'data':c
    }
    return render (request,'mns1.html',context)
def Add_Resources(request):
    if request.method == 'POST':
        form = UploadFileFrom(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            Department = form.cleaned_data['Department']
            Course = form.cleaned_data['Course']
            texxt = form.cleaned_data['texxt']
            type=form.cleaned_data['type']
            
            file = form.cleaned_data['file']
            
            new_resource = add_resources(email=email, Department=Department,type=type, Course=Course,texxt=texxt, file=file)
            new_resource.save()
            return HttpResponse('upload')
        return HttpResponse('error')
    else:
        form = UploadFileFrom()
        
    return render(request, 'Add_resources.html', {'form': form})
def show_file(request):
    # this for testing 
    all_data = add_resources.objects.all()
    

    context = {
        'data':all_data 
        }

    return render(request, 'view.html', context)
def searchfunc(request):
    
    if request.method == 'GET':
        query=request.GET['query']
 
        facul=faculty.objects.filter(initial__icontains=query)
        if len(facul)>0:
            context = {
            'data':facul 
            }
            return render (request,'search2.html',context)
        else:
            course_list = add_resources.objects.filter(Course__icontains=query)
            c = {}
            for i in course_list:
                if i.Course in c:
                    c[i.Course]+=[i]
                else:
                    c[i.Course]=[i]
            print(c)
            context={
                'data':c
            }
            return render (request,'search.html',context)
    return render(request, 'index.html')

def Faculty(request):
    if request.method == 'POST':
        form= Facultyinfo(request.POST, request.FILES)
        if form.is_valid():
            g_suit = form.cleaned_data['g_suit']
            initial = form.cleaned_data['initial']
            room_no = form.cleaned_data['room_no']
            
            file = form.cleaned_data['file']
            
            new_resource = faculty(g_suit=g_suit, initial=initial, room_no=room_no, file=file)
            new_resource.save()
            return HttpResponse('upload')
        return HttpResponse('error')
    else:
        form = Facultyinfo()
        
    return render(request, 'faculty.html', {'form': form})
def show_file1(request):
    all_data = faculty.objects.all()
    

    context = {
        'data':all_data 
        }

    return render(request, 'fac.html', context)