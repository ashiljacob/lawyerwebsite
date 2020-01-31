from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from .models import User, Lawyer, Case


def main_home(request):
    return render(request, 'index.html')


# First Page

def law(request):
    return render(request, 'lawyer.html')


def admin(request):
    return render(request, 'admin.html')


# User views
def user(request):
    return render(request, 'user.html')


def user_dash(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member1 = User.objects.get(username=request.POST['username'], password=request.POST['password'])

            #getting id of the user

            request.session['id'] = member1.id
            lawyer1 = Lawyer.objects.all()
            return render(request, 'user-dash.html', {'member': member1, 'lawyer': lawyer1})

        else:
            return render(request, 'user.html')


def registration(request):
    return render(request, 'user-registration.html')


def reg_upload(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password1']:

            reg = User(name=request.POST['name'], username=request.POST['username']
                       , password=request.POST['password'], email=request.POST['email'])
            reg.save()
            return render(request, 'user.html')
        else:
            return HttpResponse("<script>alert('Password didnt match')</script>")
            return redirect('/')
    else:
        return HttpResponse("<h1>Error While Registering.. TRy Again..</h1>")



def casefiling(request):
    if request.method == "POST" :
        a = User.objects.get(id=request.session['id'])
        print(a.name)
        case = Case(name=a.name, case=request.POST['case']
                   , caseno=request.POST['caseno'], lawyer=request.POST['lawyer'])
        case.save()
        # print(request.session['id'])
        #User.objects.filter(id=request.POST[request.session['id']])
        # law = User.objects.create(caseno=request.POST['caseno'], case=request.POST['case'])
        # return redirect("/")
        return HttpResponseRedirect(reverse("app1.url.reg_upload"))
    else:
        return HttpResponse("<h1>Error While  Case Registering.. TRy Again..</h1>")
# lawyer login --> Lawyer dashboard
def lawyerdash(request):
    if request.method == 'POST':
        if Lawyer.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            lawyer = Lawyer.objects.get(username=request.POST['username'], password=request.POST['password'])
            user = User.objects.filter(lawyer=lawyer.name)
            print(lawyer.name)

            return render(request, 'lawyerpage.html', {'lawyer': lawyer,'user':user})



    else:
        return HttpResponse("<h1>Not found.........</h2>")


def test(request):
    return HttpResponse("<h1> Hbihviwhvnv hhvhw n</h1>")
