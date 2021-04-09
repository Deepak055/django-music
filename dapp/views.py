#from dapp.forms import NewUserForm
#from dapp.models import employee
from dapp.forms import UserForm
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


"""def employee_view(request):
    employees=employee.objects.all()
    return render(request, 'dapp/hl.html',{'employee':employees})"""

def index(request):
    return render(request,'dapp/form_page.html')


def gal(request):
    return render(request,'dapp/gallery.html')

@login_required
def special(request):
    return HttpResponse('YOU LOGGED IN')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def users (request):
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserForm()
    return render(request,'dapp/users.html',{'user_form':user_form,
                                             'registered':registered})



    return render(request,'dapp/users.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
              if user.is_active:
                  login(request,user)
                  return HttpResponseRedirect(reverse('index'))
              else:
                  return HttpResponse('Account non active')
        else:
            print('some')
            print("username:{} and password{}".format(username,password))
            return HttpResponse('invalid login')
    else:
        return render(request,'dapp/login.html',{})