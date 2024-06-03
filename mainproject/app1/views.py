from django.shortcuts import render , redirect
from .models import admission
from .models import admission2
from .models import feedbackform
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm




def logout(request):
   return render(request, 'logout.html')
def home01(request):
   return render(request, 'home01.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log innow!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


# Create your views here.
def web(request):
    template = loader.get_template('webpage.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())
def feedback(request):
    template = loader.get_template('feedbackform.html')
    return HttpResponse(template.render())
def admissionform(request):
    template = loader.get_template('admission form.html')
    return HttpResponse(template.render())





def home1(request):  # 127.0.0.1:8000/
    mydata = admission.objects.all()
    if (mydata != ""):
        return render(request, "admission form.html", {"admission": mydata})
    else:
        return render(request, "admission form.html")

def home2(request):  # 127.0.0.1:8000/
    mydata2 = feedbackform.objects.all()
    if (mydata2 != ""):
        return render(request, "feedbackform.html", {"feedbackform": mydata2})
    else:
        return render(request, "feedbackform.html")

def home3(request):  # 127.0.0.1:8000/
    mydata3 = admission2.objects.all()
    if (mydata3 != ""):
        return render(request, "webpage.html", {"admission2": mydata3})
    else:
        return render(request, "webpage.html")

def add(request):
    if request.method == "POST":
        name1 = request.POST["name"]
        con = request.POST["contact"]
        mail = request.POST["email"]
        password1 = request.POST["password"]
        pass2 = request.POST["pass01"]

        obj = admission()
        obj.name = name1
        obj.contact = con
        obj.email = mail
        obj.Password = password1
        obj.pass01 = pass2

        obj.save()
        mydata = admission.objects.all()
        return redirect("home1")
    return render(request, "admission form.html")


def add1(request):
    if request.method == "POST":
        name1 = request.POST["fname"]
        name2 = request.POST["lname"]
        con = request.POST["contact"]
        sub = request.POST["subject"]


        obj= feedbackform()
        obj.fname = name1
        obj.lname = name2
        obj.contact = con
        obj.subject = sub
        obj.save()
        mydata2 = feedbackform.objects.all()
        return redirect("home2")
        return render(request, "feedbackform.html")

def addata(request):
    if request.method == "POST":
        name1 = request.POST["name"]
        con = request.POST["contact"]
        mail = request.POST["email"]
        password1 = request.POST["Psw"]
        pass2 = request.POST["psw2"]

        obj = admission2()
        obj.name = name1
        obj.contact = con
        obj.email = mail
        obj.Psw = password1
        obj.psw2 = pass2

        obj.save()
        mydata3 = admission2.objects.all()
        return redirect("home3")
    return render(request, "webpage.html")